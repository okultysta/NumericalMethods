import numpy as np

def polynomial(x):
    #4x^4 +2x^3 +8x^2 +5x +5
    return x*(x*(x*(4*x+2)+8)+5)+5

def exponential(x):
    wynik = x
    for i in range(2,5):
        wynik*=wynik
    return wynik

def trigonometric(x):
    return 2 * np.cos(x) * np.sin(x) + 10*np.cos(3*x) / np.sin(x/2)


######### FUNCTIONS FOR TESTS ############

def one_root(x):
    return x-2

def one_root_2(x):
    return x-1.43275294722938562918374

def two_roots(x):
    return x*(x-6)+8

def tree_roots(x):
    return (x-1.237261)*(x-2.437983)*(x-3.9726334)