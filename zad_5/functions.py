import numpy as np

def polynomial(x):

    wspolczynniki = [0.5, 0.2, -5, 3]  # Przykładowe współczynniki
    length = len(wspolczynniki)
    result = wspolczynniki[0]
    for i in range(1, length):
        result = result * x + wspolczynniki[i]
    return result


def exponential(x):

    return np.exp(0.5 * x) - 5


def trigonometric(x):

    return np.sin(2 * x) / (x + 0.5)


def absolute_value(x):

    return np.abs(x) - 2


def mixed(x):
    return np.exp(0.2 * x) - 5 * np.cos(x / 2)
