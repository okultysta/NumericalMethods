
#a, b - krańce przedziałów
#stop_war -  warunek stopu (0 - zadana dokładnosc lub 1 - zadana liczb iteracji)
#war_value - wartosc warunku stopu (0 - epsilon, 1 - liczba iteracji)
def bisection_method(a, b, stop_war, war_value):
    x = (a+b)/2

    return