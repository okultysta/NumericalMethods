import numpy as np
from math import sqrt, cos, pi


def f(x):
    # Przykładowa funkcja f(x) = x^2
    return x**2


def simpson_with_weight(func, a, b, eps=1e-6, max_iter=20):
    def weighted_f(x):
        if abs(x) == 1:
            return 0  # unika dzielenia przez 0
        return func(x) / sqrt(1 - x**2)

    def simpson_rule(f, a, b, n):
        if n % 2 == 1:
            n += 1
        h = (b - a) / n
        result = f(a) + f(b)
        for i in range(1, n):
            coeff = 4 if i % 2 == 1 else 2
            result += coeff * f(a + i * h)
        return result * h / 3

    total_integral = 0
    segments = [(0, 0.5)]
    factor = 0.5
    for i in range(10):
        start = segments[-1][1]
        width = factor * (1 / 2**(i + 1))
        end = start + width
        segments.append((start, end))

    for (left, right) in segments:
        prev = simpson_rule(weighted_f, left, right, 2)
        for n in range(4, 2**max_iter + 1, 2):
            current = simpson_rule(weighted_f, left, right, n)
            if abs(current - prev) < eps:
                break
            prev = current
        total_integral += current
        total_integral += simpson_rule(weighted_f, -right, -left, n)

    return total_integral


def gauss_chebyshev(func, n=5):
    result = 0
    for k in range(1, n + 1):
        x_k = cos((2 * k - 1) * pi / (2 * n))
        result += func(x_k)
    return pi / n * result

