import numpy as np
import math

def polynomial(x):
    wspolczynniki = [1, 0.47, -80.8248, -19.2608, 990.2336]
    length = 5
    result = wspolczynniki[0]
    for i in range(1, length):
        result = result*x + wspolczynniki[i]
    return result

def exponential(x):
    return 2**x - 100

"""
    if x<0:
        return 1/math.exp(-x)-100
    else:
        return math.exp(-x)-100
"""

"""
    x = np.atleast_1d(x)
    for num in x:
        result = 1
        if num < 0:
            return 1 / exponential(-num)
        if num == 0:
            return 1
        if num % 1 == 0:
            num = int(num)
            for i in range(num):
                result *= num
            return result - 100
        else:
            result = 2 ** num
            return result - 100
"""

def trigonometric(x):
    return np.sin(x)-0.5

def mixed(x):
    return np.exp(x)-1000*(np.cos(x/2))-250

def const_zero(x):
    return x*0


######### FUNCTIONS FOR TESTS ############

def one_root(x):
    return x-2

def one_root_2(x):
    return x-1.43275294722938562918374

def two_roots(x):
    return x*(x-6)+8

def tree_roots(x):
    return (x-1.237261)*(x-2.437983)*(x-3.9726334)
