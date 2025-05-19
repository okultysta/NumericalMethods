import numpy as np
import matplotlib.pyplot as plt


def gauss_laguerre_quadrature(f, n):
    """
    Całkowanie metodą Gaussa-Laguerre'a.
    Zakres całkowania: [0, ∞).
    """
    x, w = np.polynomial.laguerre.laggauss(n)
    return sum(w * f(x))


def laguerre(n, x):
    """ Obliczanie wielomianów Laguerre'a iteracyjnie. """
    if n == 0:
        return 1
    elif n == 1:
        return 1 - x
    else:
        L0, L1 = 1, 1 - x
        for k in range(2, n + 1):
            L0, L1 = L1, ((2 * k - 1 - x) * L1 - (k - 1) * L0) / k
        return L1


def horner_scheme(coeffs, x):
    """ Schemat Hornera do szybkiego obliczania wartości wielomianu """
    result = coeffs[0]
    for coeff in coeffs[1:]:
        result = result * x + coeff
    return result


def approximate(function, degree, nodes=10):
    coeffs = []
    for n in range(degree + 1):
        integrand = lambda x: function(x) * laguerre(n, x)
        coeff = gauss_laguerre_quadrature(integrand, nodes)
        coeffs.append(coeff)
    return coeffs


def plot_approximation(function, coeffs, a, b):
    x_values = np.linspace(a, b, 500)
    y_original = [function(x) for x in x_values]
    y_approx = [horner_scheme(coeffs, x) for x in x_values]

    plt.plot(x_values, y_original, label="Funkcja oryginalna")
    plt.plot(x_values, y_approx, label="Aproksymacja (Laguerre)", linestyle='--')
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_error(function, coeffs, a, b, points=1000):
    x_values = np.linspace(a, b, points)
    error = sum((function(x) - horner_scheme(coeffs, x)) ** 2 for x in x_values)
    return error / points
