import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.special import roots_laguerre
import math


def horner(coeffs, x):
    result = coeffs[-1]
    for i in range(len(coeffs) - 2, -1, -1):
        result = result * x + coeffs[i]
    return result


def laguerre_polynomials(n, x):
    x = np.array(x, dtype=float)
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 1.0 - x
    L0 = np.ones_like(x)
    L1 = 1.0 - x
    for k in range(2, n + 1):
        L2 = ((2 * k - 1 - x) * L1 - (k - 1) * L0) / k
        L0, L1 = L1, L2
    return L1


def laguerre_coefficient(func, n, nodes):
    x_k, w_k = roots_laguerre(nodes)
    return np.sum(w_k * func(x_k) * laguerre_polynomials(n, x_k))


def approximate(func, degree, nodes):
    coeffs = []
    for n in range(degree + 1):
        a_n = laguerre_coefficient(func, n, nodes)
        coeffs.append(a_n)
    print_standard_polynomial(coeffs)
    return coeffs


def evaluate_laguerre_series(coeffs, x):
    result = np.zeros_like(x, dtype=float)
    for n, a_n in enumerate(coeffs):
        result += a_n * laguerre_polynomials(n, x)
    return result


def plot_approximation(func, coeffs, a, b):
    x_vals = np.linspace(a, b, 500)
    y_true = func(x_vals)
    y_approx = evaluate_laguerre_series(coeffs, x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_true, label='Funkcja oryginalna', color='blue')
    plt.plot(x_vals, y_approx, label='Aproksymacja Laguerrea', linestyle='--', color='red')
    plt.title('Porównanie funkcji oryginalnej i aproksymacji Laguerrea')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()


def calculate_error(func, coeffs, a, b, num_points=1000):
    x_vals = np.linspace(a, b, num_points)
    y_true = func(x_vals)
    y_approx = evaluate_laguerre_series(coeffs, x_vals)
    error = np.sqrt(np.mean((y_true - y_approx) ** 2))
    return error


def print_laguerre_polynomial(coeffs):
    terms = []
    for n, a_n in enumerate(coeffs):
        if abs(a_n) < 1e-10:
            continue
        if n == 0:
            terms.append(f"{a_n:.4f}")
        elif n == 1:
            terms.append(f"{a_n:.4f}·L₁(x)")
        else:
            terms.append(f"{a_n:.4f}·L{n}(x)")
    polynomial = " + ".join(terms)
    print("Wielomian aproksymujący :")
    print(f"P(x) ≈ {polynomial}")


def get_standard_laguerre(n):
    coeffs = [0] * (n + 1)
    for k in range(n + 1):
        coeffs[k] = ((-1) ** k) * math.comb(n, k) / math.factorial(k)
    return coeffs


def print_standard_polynomial(coeffs):
    max_deg = len(coeffs) - 1
    final_coeffs = np.zeros(max_deg + 20)

    for n, a_n in enumerate(coeffs):
        laguerre_coeffs = get_standard_laguerre(n)
        for i, c in enumerate(laguerre_coeffs):
            final_coeffs[i] += a_n * c

    # NIE usuwamy końcowych zer – chcemy stopień = max_deg

    print("Wielomian aproksymujący w postaci standardowej (do stopnia n):")

    terms = []
    for i in reversed(range(max_deg + 1)):
        c = final_coeffs[i]
        if i == 0:
            terms.append(f"{c:.16e}")
        elif i == 1:
            terms.append(f"{c:.16e}·x")
        else:
            terms.append(f"{c:.16e}·x^{i}")

    print(" + ".join(terms))

