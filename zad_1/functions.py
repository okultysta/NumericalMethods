import numpy as np

def polynomial(x):
    return (x+8.2938491)*(x+1.484719)*(x-3.92837492)*(x-8.9999998)

def exponential(x):
    return (2**x)-100

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
