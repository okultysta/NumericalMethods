import integrals

def f(x):
    # Przykładowa funkcja f(x) = x^2
    return x**2

print("Całkowanie funkcji f(x) = x^2 z wagą 1/sqrt(1 - x^2) na przedziale [-1, 1]")

# Kwadratura Newtona-Cotesa (Simpson)
simpson_result = integrals.simpson_with_weight(f, -1, 1, eps=1e-6)
print(f"Wynik metody Simpsona (złożonej): {simpson_result:.10f}")

# Kwadratura Gaussa-Czebyszewa
for n in [2, 3, 4, 5]:
    gauss_result = integrals.gauss_chebyshev(f, n)
    print(f"Wynik kwadratury Gaussa-Czebyszewa (n={n}): {gauss_result:.10f}")

