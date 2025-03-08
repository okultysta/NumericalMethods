import numpy as np

def polynomial(x):
    return (x+8.2938491)*(x+1.484719)*(x-3.92837492)*(x-8.9999998)

def exponential(x):
    wynik = x
    for i in range(2,5):
        wynik*=wynik
    return wynik

def trigonometric(x):
    return 2 * np.cos(x) * np.sin(x) + 10*np.cos(3*x) / np.sin(x/2)

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