import numpy as np

def polynomial(x):
    wspolczynniki = [1, 0.47, -80.8248, -19.2608, 990.2336]
    length = 5
    result = wspolczynniki[0]
    for i in range(1, length):
        result = result * x + wspolczynniki[i]
    return result


def exponential(x):
    return 2 ** x - 100


def trigonometric(x):
    return np.sin(x) - 0.5


def mixed(x):
    return np.exp(x) - 1000 * (np.cos(x / 2)) - 250


def const_zero(x):
    return x * 0


######### FUNCTIONS FOR TESTS ############

def one_root(x):
    return x - 2


def one_root_2(x):
    return x - 1.43275294722938562918374


def two_roots(x):
    return x * (x - 6) + 8


def tree_roots(x):
    return (x - 1.237261) * (x - 2.437983) * (x - 3.9726334)
