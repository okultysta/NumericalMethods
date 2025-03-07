import numpy as np

#a, b - krańce przedziałów
#stop_war -  warunek stopu (0 - zadana dokładnosc lub 1 - zadana liczb iteracji)
#war_value - wartosc warunku stopu (0 - epsilon, 1 - liczba iteracji)
#function - wybrana funkcja
def bisection_iteration(a, b, function, iterations):
    x = 0
    old_x = 0
    for i in range(iterations):
        x = (a+b)/2
        if function(x):
            return x, x
        elif function(x)*function(a)<0:
            b=x
        else:
            a=x
        old_x = x
    return x, (x - old_x)

def bisection_epsilon(a,b,function,epsilon):
    x = a
    old_x = b
    iterations = 1
    while x - old_x > epsilon:
        x = (a+b)/2
        if function(x):
            return x, iterations
        elif function(x)*function(a)<0:
            b=x
        else:
            a=x
        old_x = x
        iterations += 1
    return x, iterations


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