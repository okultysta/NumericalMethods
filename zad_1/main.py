import algorithms
import functions

print("wybierz funkcję z podanych wpisując cyfrę znajdująca się obok funkcji:")
print("1.wielomian")
print("2.Trygonometryczna")
print("3.wykładnicza")
print("4.Złorzenie")

function = functions.polynomial
not_chosen = True

while True:
    choice = input("Wpisz numer wybranej funkcji [1/2/3/4]:")
    if choice == "1":
        print("wybrales funkcje wielomian")
        function = functions.polynomial
        break
    elif choice == "2":
        print("wybrales funkcje trygonometryczna")
        function = functions.trigonometric
        break
    elif choice == "3":
        print("wybrales funkcje wykladnicza")
        function = functions.exponential
        break
    elif choice == "4":
        print("wybrales funkcje zlozenia")
        #function = functions.polynomial
        break
    else:
        print("podano niewłasciwa wartosc. Sprobuj ponownie.")

a,b = 0, 0
print("Wybierz przedzial, na ktorym program ma znalezc miejsce zerowe, podajac poczatek i koniec przedzialu:")
while True:
    a = input("Podaj poczatek przedzialu:")
    b = input("Podaj koniec przedzialu:")
    a = float(a)
    b = float(b)
    if function(a)*function(b)>=0:
        print("Podano niewlasciwe wartosci. Wartosci funkcji na krancach przedzialu musza miec przeciwne znaki.")
        print("Wartosci funkcji dla podanych wartosci wynosza odpowiednio:")
        print("Wartosc funkcji w punkcie poczatkowym przedzialu:" + str(function(a)))
        print("Wartosc funkcji w punkcie koncowym przedzialu:" + str(function(b)))
        print()
        print("Sprobuj wybran krance przedzialu ponownie.")
    else:
        break

stop_con = ""
iter_epsilon = 0
print("Wybierz kryterium zatrzymania dla algorytmu poprzez wpisanie odpowiadajacej mu liczby:")
print("1.Liczba iteracji - algorytm zakonczy dzialanie i zwroci wynik po wykonaniu okreslonej liczby iteracji")
print("2.Dokladnosc wyniku - algorytm zakonczy  i zwroci wynik po osiagnieciu okreslonej dokladnosci")

while True:
    stop_con = input("Podaj warunek stopu [1/2]:")
    if stop_con == "1":
        print("Wybrales kryterium iteracyjne.")
        while True:
            print("UWAGA: Liczba iteracji musi byc liczba calkowita oraz nie moze byc mniejsza od 1!")
            iter_epsilon = input("Podaj liczbe iteracji jaka program ma przeprowadzic:")
            iter_epsilon = int(iter_epsilon)
            if iter_epsilon < 1:
                print("Podana wartosc jest niewlasciwa (mniejsza od 1). Sprobuj ponownie.")
            else:
                break
        break

    elif stop_con == "2":
        print("Wybrales kryterium dokladnosci wyniku.")
        while True:
            print("UWAGA: Wartosc epsilon musi byc wieksza od zera!")
            iter_epsilon = input("Podaj wartosc epsilon dla dokladnosci, po osiagnieciu ktorej algorytm zakoczy dzialanie")
            iter_epsilon = int(iter_epsilon)
            if iter_epsilon < 0:
                print("Podana wartosc jest niewlasciwa (mniejsza od 0). Sprobuj ponownie.")
            else:
                break
        break
    else:
        print("Podano niewlasciwa opcje (Brak wybranej opcji). Sprobuj ponownie.")

approx = 0
done_epsilon_iter = 0
if stop_con == "1":
    approx,done_epsilon_iter = algorithms.bisection_iteration(a,b,function,iter_epsilon)
else:
    approx,done_epsilon_iter = algorithms.bisection_epsilon(a,b,function,iter_epsilon)