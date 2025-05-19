import numpy as np

def polynomial(x):
    wspolczynniki = [0.5, 0.2, -5, 3]  # Przykładowe współczynniki
    length = len(wspolczynniki)
    result = wspolczynniki[0]
    for i in range(1, length):
        result = result * x + wspolczynniki[i]
    return result

def exponential(x):
    return np.exp(0.5 * x) - 5

def trigonometric(x):
    return np.sin(2 * x) / (x + 0.5)

def absolute_value(x):
    return np.abs(x)

def mixed(x):
    return np.exp(0.2 * x) - 5 * np.cos(x / 2)

from approximation import (
    approximate,
    plot_approximation,
    calculate_error
)

def choose_function():
    print("Wybierz funkcję z podanych wpisując cyfrę znajdującą się obok funkcji:")
    print("1. Wielomian: 0.5x³ + 0.2x² - 5x + 3")
    print("2. Trygonometryczna: sin(2x)/(x + 0.5)")
    print("3. Wykładnicza: e^(0.5x) - 5")
    print("4. Wartość bezwzględna: |x|")
    print("5. Złożenie: e^(0.2x) - 5cos(x/2)")

    while True:
        choice = input("Wpisz numer wybranej funkcji [1/2/3/4/5]: ")
        if choice == "1":
            return polynomial, "wielomian"
        elif choice == "2":
            return trigonometric, "trygonometryczna"
        elif choice == "3":
            return exponential, "wykładnicza"
        elif choice == "4":
            return absolute_value, "moduł"
        elif choice == "5":
            return mixed, "złożenie"
        else:
            print("BŁĄD: Brak wybranej opcji. Spróbuj ponownie.")

def main_manual():
    function, name = choose_function()
    degree = int(input("Podaj stopień wielomianu aproksymacyjnego: "))
    nodes = int(input("Podaj liczbę węzłów aproksymacji: "))
    a = float(input("Podaj początek przedziału aproksymacji: "))
    b = float(input("Podaj koniec przedziału aproksymacji: "))

    coeffs = approximate(function, degree, nodes)
    plot_approximation(function, coeffs, a, b)

    error = calculate_error(function, coeffs, a, b)
    print(f"Średni błąd aproksymacji: {error}")

def main_auto():
    function, name = choose_function()
    nodes = int(input("Podaj liczbę węzłów aproksymacji: "))
    a = float(input("Podaj początek przedziału aproksymacji: "))
    b = float(input("Podaj koniec przedziału aproksymacji: "))
    target_error = float(input("Podaj oczekiwany maksymalny błąd aproksymacji: "))

    degree = 1
    while degree <= 50:
        coeffs = approximate(function, degree, nodes)
        error = calculate_error(function, coeffs, a, b)
        print(f"Stopień: {degree}, błąd aproksymacji: {error}")

        if error <= target_error:
            print(f"Osiągnięto oczekiwany błąd {error} przy stopniu {degree}.")
            plot_approximation(function, coeffs, a, b)
            break
        degree += 1
    else:
        print("Osiągnięto maksymalny stopień (50) bez osiągnięcia wymaganego błędu.")

if __name__ == "__main__":
    print("Wybierz tryb pracy programu:")
    print("1 - Ręczne podanie stopnia wielomianu")
    print("2 - Automatyczny dobór stopnia na podstawie błędu aproksymacji")
    mode = input("Twój wybór [1/2]: ")

    if mode == "1":
        main_manual()
    elif mode == "2":
        main_auto()
    else:
        print("Nieznany tryb. Kończę.")