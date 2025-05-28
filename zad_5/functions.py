import numpy as np

def polynomial(x):

    wspolczynniki = [2, -4, 8, -3]  # Przykładowe współczynniki
    length = len(wspolczynniki)
    result = wspolczynniki[0]
    for i in range(1, length):
        result = result * x + wspolczynniki[i]
    return result

def linear(x):
    return 2*x+3
def exponential(x):

    return np.exp(0.5 * x) - 5


def trigonometric(x):

    return np.cos(x)


def absolute_value(x):

    return np.abs(x)


def mixed(x):
    return np.exp(0.2 * x) - 5 * np.cos(x / 2)
