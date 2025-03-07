import numpy as np

#a, b - krańce przedziałów
#stop_war -  warunek stopu (0 - zadana dokładnosc lub 1 - zadana liczb iteracji)
#war_value - wartosc warunku stopu (0 - epsilon, 1 - liczba iteracji)
#function - wybrana funkcja
def bisection_method(a, b, function, epsilon=1e-6, max_iterations=100, compart_count=100):
    result = []
    compartments = np.linspace(a, b, compart_count)
    for i in range(len(compartments)-1):
        x1, x2 = compartments[i], compartments[i + 1]
        if function(x1) * function(x2) > 0:
            iterations = 0
            while iterations < max_iterations and (x2-x1) > epsilon:
                x = (x1+x2/2)
                if function(x)==0:
                    result.append(x)
                elif function(x)*function(b)<0:
                    x1 = x
                else:
                    x2 = x
                iterations += 1

            result.append((x1+x2)/2)

    return result


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