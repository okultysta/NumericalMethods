import algorithms
import functions
import numpy as np
import matplotlib.pyplot as plt

#czy horner moze tak wygladac
#czy tak moze wygladac wyliczanie dokladnosci

print()
print("Wybierz funkcję z podanych wpisując cyfrę znajdująca się obok funkcji:")
print()
print("1.wielomian: (x+8.2938491)*(x+1.484719)*(x-3.92837492)*(x-8.9999998)")
print("2.Trygonometryczna: sin(x) - 0.5")
print("3.wykładnicza: 2^x - 100")
print("4.Złorzenie: e^x - 1000*cos(x/2) - 250")

function = functions.polynomial
not_chosen = True
flag = True

while flag:
    print()
    choice = input("Wpisz numer wybranej funkcji [1/2/3/4]:")
    if choice == "1":
        print("wybrales funkcje wielomian")
        function = functions.polynomial
        flag = False
    elif choice == "2":
        print("wybrales funkcje trygonometryczna")
        function = functions.trigonometric
        flag = False
    elif choice == "3":
        print("wybrales funkcje wykladnicza")
        function = functions.exponential
        flag = False
    elif choice == "4":
        print("wybrales funkcje zlozenia")
        function = functions.mixed
        flag = False
    else:
        print()
        print("BLAD: Brak wybranej opcji. Sprobuj ponownie.")

flag = True
print("Obejrzyj wykres wybranej funkcji.")
print()

x_values = np.arange(-10, 10.1, 0.1)
y_values = function(x_values)
x_axis = functions.const_zero(x_values)

plt.figure(num=0, dpi=300)
plt.plot(x_values, y_values)
plt.plot(x_values, x_axis, color="black")
plt.title("Wykres pokazowy")
plt.show()

a,b = 0, 0
print("Wybierz przedzial, na ktorym program ma znalezc miejsce zerowe, podajac poczatek i koniec przedzialu:")
while flag:
    a = input("Podaj poczatek przedzialu:")
    b = input("Podaj koniec przedzialu:")
    a = float(a)
    b = float(b)
    if a == b:
        print()
        print("BLAD: Poczatek i koniec przedzialu nie moga byc takie same. Sprobuj ponownie.")
    elif a > b:
        print()
        print("BLAD: Koniec przedzialu nie moze byc mniejszy od jego poczatku. Sprobuj ponownie.")
    elif function(a)*function(b)>=0:
        print()
        print("BLAD: Podano niewlasciwe wartosci. Wartosci funkcji na krancach przedzialu musza miec przeciwne znaki.")
        print("Wartosci funkcji dla podanych wartosci wynosza odpowiednio:")
        print("Wartosc funkcji w punkcie poczatkowym przedzialu:" + str(function(a)))
        print("Wartosc funkcji w punkcie koncowym przedzialu:" + str(function(b)))
        print()
        print("Sprobuj wybran krance przedzialu ponownie.")
        print()
    else:
        flag = False

flag = True
flag2 = True
stop_con = ""
iter_epsilon = 0
print()
print("Wybierz kryterium zatrzymania dla algorytmu poprzez wpisanie odpowiadajacej mu liczby:")
print()
print("1.Liczba iteracji - algorytm zakonczy dzialanie i zwroci wynik po wykonaniu okreslonej liczby iteracji")
print("2.Dokladnosc wyniku - algorytm zakonczy  i zwroci wynik po osiagnieciu okreslonej dokladnosci")
print()

while flag:
    stop_con = input("Podaj warunek stopu [1/2]:")
    print()
    if stop_con == "1":
        print("Wybrales kryterium iteracyjne.")
        while flag2:
            print()
            print("UWAGA: Liczba iteracji musi byc liczba calkowita oraz nie moze byc mniejsza od 1!")
            iter_epsilon = input("Podaj liczbe iteracji jaka program ma przeprowadzic:")
            iter_epsilon = int(iter_epsilon)
            if iter_epsilon < 1:
                print()
                print("BLAD: Podana wartosc jest niewlasciwa (mniejsza od 1). Sprobuj ponownie.")
            else:
                flag2 = False
        flag = False

    elif stop_con == "2":
        print("Wybrales kryterium dokladnosci wyniku.")
        while flag2:
            print()
            print("UWAGA: Wartosc epsilon musi byc wieksza od zera!")
            iter_epsilon = input("Podaj wartosc epsilon dla dokladnosci, po osiagnieciu ktorej algorytm zakoczy dzialanie:")
            iter_epsilon = float(iter_epsilon)
            if iter_epsilon < 0:
                print()
                print("BLAD: Podana wartosc jest niewlasciwa (mniejsza od 0). Sprobuj ponownie.")
            else:
                flag2 = False
        flag = False
    else:
        print()
        print("BLAD: Podano niewlasciwa opcje (Brak wybranej opcji). Sprobuj ponownie.")
        print()

bi_approx = 0
bi_accur_iter = 0
fa_approx = 0
fa_accur_iter = 0

print()
print("------------------------- Wyliczono przyblizone wartosci miejsc zerowych oboma metodami. Oto wyniki ---------------------------------")
print()

if stop_con == "1":
    bi_approx, bi_accur_iter = algorithms.bisection_iteration(a,b,function,iter_epsilon)
    fa_approx, fa_accur_iter = algorithms.falsi_iteration(a,b,function,iter_epsilon)
    print("####### Wartosci wyliczone algorytmem Bisekcji #######")
    print("Przyblizona wartosc miejsca zerowego: ", bi_approx)
    print("wyliczona dokladnosc przyblizenia: ", bi_accur_iter)
    print()
    print("####### Wartosci wyliczone Regula Falsi #######")
    print("Przyblizona wartosc miejsca zerowego: ", fa_approx)
    print("wyliczona dokladnosc przyblizenia: ", fa_accur_iter)
else:
    bi_approx, bi_accur_iter = algorithms.bisection_epsilon(a,b,function,iter_epsilon)
    fa_approx, fa_accur_iter = algorithms.falsi_epsilon(a,b,function,iter_epsilon)
    print("#######Wartosci wyliczone algorytmem Bisekcji#######")
    print("Przyblizona wartosc miejsca zerowego: ", bi_approx)
    print("Liczba wykonanych iteracji: ", bi_accur_iter)
    print()
    print("#######Wartosci wyliczone Regula Falsi#######")
    print("Przyblizona wartosc miejsca zerowego: ", fa_approx)
    print("Liczba wykonanych iteracji: ", fa_accur_iter)

print()
print("Wartosci te przedstawiono na 3 wykresach")

plt.figure(num=0, dpi=300)
plt.plot(x_values, y_values)
plt.plot(x_values, x_axis, color="black")
plt.plot(bi_approx, 0, marker='^', color='green', label='Algorytm Bisekcji')
plt.plot(fa_approx, 0, marker='o', color='red', label='Reguła Falsi')
plt.title("Wykres na przedzialem takim jak na wykresie pokazowym")
plt.legend()
plt.show()

x_values = np.arange(a, b+0.1, 0.1)
y_values = function(x_values)
x_axis = functions.const_zero(x_values)

plt.figure(num=1, dpi=300)
plt.plot(x_values, y_values)
plt.plot(x_values, x_axis, color="black")
plt.plot(bi_approx, 0, marker='^', color='green', label='Algorytm Bisekcji')
plt.plot(fa_approx, 0, marker='o', color='red', label='Reguła Falsi')
plt.title("Wykres na wybranym przez uzytkownika przedziale")
plt.legend()
plt.show()

length = abs(bi_approx-fa_approx)

a = min(bi_approx, fa_approx) - length/2
b = max(bi_approx, fa_approx) + length/2

x_values = np.linspace(a, b, 100)
y_values = function(x_values)
x_axis = functions.const_zero(x_values)

plt.figure(num=1, dpi=300)
plt.plot(x_values, y_values)
plt.plot(x_values, x_axis, color="black")
plt.plot(bi_approx, 0, marker='^', color='green', label='Algorytm Bisekcji')
plt.plot(fa_approx, 0, marker='o', color='red', label='Reguła Falsi')
plt.title("wykres z przedzialem dostosowanym do osiagnietych wynikow")
plt.legend()
plt.show()