import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from scipy.special import roots_laguerre


# Wielomiany Laguerre'a (poprawione)
def laguerre(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 1 - x
    L_prev, L_curr = np.ones_like(x), 1 - x
    for k in range(1, n):
        L_next = ((2 * k + 1 - x) * L_curr - k * L_prev) / (k + 1)
        L_prev, L_curr = L_curr, L_next
    return L_curr


# Całkowanie Gaussa-Laguerre'a
def gauss_laguerre_integrate(f, n):
    nodes, weights = roots_laguerre(n)
    return np.sum(weights * f(nodes))


# Aproksymacja funkcji
def approximate(f, degree, nodes):
    coefficients = np.zeros(degree + 1)
    for k in range(degree + 1):
        integrand = lambda x: f(x) * laguerre(k, x)
        coefficients[k] = gauss_laguerre_integrate(integrand, nodes) / factorial(k) ** 2
    return coefficients


# Obliczanie wartości aproksymowanej funkcji
def approx_function(x, coefficients):
    return sum(c * laguerre(k, x) for k, c in enumerate(coefficients))



def calculate_error(f, coefficients, a=0, b=10, nodes=6):
    # Definiujemy funkcję błędu z wagą e^(-x)
    def error_func(x):
        return (f(x) - approx_function(x, coefficients))**2 * np.exp(-x)

    # Jeśli chcemy policzyć na przedziale [a, b] - używamy Legendre
    if b < np.inf:
        from scipy.special import roots_legendre
        nodes, weights = roots_legendre(nodes)
        integral = 0.0
        for xi, wi in zip(nodes, weights):
            x = 0.5 * (a + b) + 0.5 * (b - a) * xi
            integral += wi * error_func(x)
        return np.sqrt(0.5 * (b - a) * integral)
    else:
        # Dla przedziału [0, inf) używamy Laguerre
        return np.sqrt(gauss_laguerre_integrate(error_func, nodes))


# Wizualizacja wyników
def plot_approximation(f, coefficients, a, b):
    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label="Oryginalna")
    plt.plot(x, approx_function(x, coefficients), label="Aproksymacja")
    plt.title("Porównanie funkcji oryginalnej i aproksymacji")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()
