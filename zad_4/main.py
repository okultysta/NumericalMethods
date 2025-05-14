import math

import integrals
import functions

print("Wybierz funkcję z podanych wpisując cyfrę znajdującą się obok funkcji:")
print("1. Wielomian")
print("2. Trygonometryczna: sin(x) - 0.5")
print("3. Wykładnicza: 2^x - 100")
print("4. Złożenie: e^x - 1000*cos(x/2) - 250")

function = functions.polynomial
name = "wielomian"
flag = True

while flag:
    choice = input("Wpisz numer wybranej funkcji [1/2/3/4]: ")
    if choice == "1":
        function = functions.polynomial
        name = "wielomian"
        flag = False
    elif choice == "2":
        function = functions.trigonometric
        name = "trygonometryczna"
        flag = False
    elif choice == "3":
        function = functions.exponential
        name = "wykładnicza"
        flag = False
    elif choice == "4":
        function = functions.mixed
        name = "złożenie"
        flag = False
    else:
        print("BŁĄD: Brak wybranej opcji. Spróbuj ponownie.")
eps = 0.00001
while True:
    try:
        eps = float(input("\nPodaj dokładność (np. 0.00001): "))
        if eps <= 0:
            raise ValueError
        break
    except ValueError:
        print("BŁĄD: Wprowadź poprawną dodatnią liczbę zmiennoprzecinkową.")


decimal_places = max(0, -int(math.floor(math.log10(eps))))

print(f"\nCałkowanie funkcji {name}  na przedziale [-1, 1]")

# Metoda Simpsona (z wagą)
simpson_result = integrals.simpson_with_weight(function, -1, 1, eps=eps)
print(f"Wynik metody Simpsona (złożonej): {simpson_result:.{decimal_places}f}")

# Metoda Gaussa-Czebyszewa dla różnych n
for n in [2, 3, 4, 5]:
    gauss_result = integrals.gauss_chebyshev(function, n)
    print(f"Wynik kwadratury Gaussa-Czebyszewa (n={n}): {gauss_result:.{decimal_places}f}")

