import math
import numpy as np
import matplotlib.pyplot as plt
import interpolation
import functions
import file_loader

filename = input("Podaj nazwę pliku z węzłami: ")
nodes = file_loader.load_from_file(filename)
nodes.sort()

print("Wczytane węzły:")
print(nodes)

print()
print("Wybierz funkcję z podanych wpisując cyfrę znajdująca się obok funkcji:")
print()
print("1.wielomian: ")
print("2.Trygonometryczna: sin(x) - 0.5")
print("3.wykładnicza: 2^x - 100")
print("4.Złożenie: e^x - 1000*cos(x/2) - 250")

function = functions.polynomial
name = "wielomian"
flag = True

while flag:
    print()
    choice = input("Wpisz numer wybranej funkcji [1/2/3/4]:")
    if choice == "1":
        print("wybrales funkcje wielomian")
        function = functions.polynomial
        name = "wielomian"
        flag = False
    elif choice == "2":
        print("wybrales funkcje trygonometryczna")
        function = functions.trigonometric
        name = "trygonometryczna"
        flag = False
    elif choice == "3":
        print("wybrales funkcje wykladnicza")
        function = functions.exponential
        name = "wykładnicza"
        flag = False
    elif choice == "4":
        print("wybrales funkcje zlozenia")
        function = functions.mixed
        name = "złożenie"
        flag = False
    else:
        print()
        print("BLAD: Brak wybranej opcji. Sprobuj ponownie.")


interp_func = interpolation.lagrange_interpolation(nodes, function)

length = max(nodes)-min(nodes)
a = min(nodes) - length/2
b = max(nodes) + length/2

x_vals = np.linspace(a, b, 100)
y_true = [function(x) for x in x_vals]
y_interp = [interp_func(x) for x in x_vals]

plt.plot(x_vals, y_true, label=name, color='blue')
plt.plot(x_vals, y_interp, label='Interpolacja Lagrange’a', linestyle='--', color='red')
plt.scatter(nodes, [function(x) for x in nodes], color='black', zorder=5, label='Węzły')
plt.legend()
plt.title("Interpolacja Lagrange’a vs "+name)
plt.grid(True)
plt.show()


a = min(nodes) - length
b = max(nodes) + length

x_vals = np.linspace(a, b, 100)
y_true = [function(x) for x in x_vals]
y_interp = [interp_func(x) for x in x_vals]

plt.plot(x_vals, y_true, label=name, color='blue')
plt.plot(x_vals, y_interp, label='Interpolacja Lagrange’a', linestyle='--', color='red')
plt.scatter(nodes, [function(x) for x in nodes], color='black', zorder=5, label='Węzły')
plt.legend()
plt.title("Interpolacja Lagrange’a vs "+name)
plt.grid(True)
plt.show()


a = min(nodes) - 2*length
b = max(nodes) + 2*length

x_vals = np.linspace(a, b, 100)
y_true = [function(x) for x in x_vals]
y_interp = [interp_func(x) for x in x_vals]

plt.plot(x_vals, y_true, label=name, color='blue')
plt.plot(x_vals, y_interp, label='Interpolacja Lagrange’a', linestyle='--', color='red')
plt.scatter(nodes, [function(x) for x in nodes], color='black', zorder=5, label='Węzły')
plt.legend()
plt.title("Interpolacja Lagrange’a vs "+name)
plt.grid(True)
plt.show()