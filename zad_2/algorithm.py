import numpy as np


def swap_rows(A, row1, row2):
    """Zamienia dwa wiersze w macierzy A."""
    A[[row1, row2]] = A[[row2, row1]]


def swap_columns(A, col1, col2):
    """Zamienia dwie kolumny w macierzy A."""
    A[:, [col1, col2]] = A[:, [col2, col1]]


def fix_diagonal_zeros(A, b, memory):
    """
    Sprawdza, czy na przekątnej macierzy A są zera i w razie potrzeby zamienia wiersze lub kolumny.
    :param A: macierz współczynników (n x n)
    :param b: wektor wynikowy (n x 1)
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    n = len(A)

    for i in range(n):
        if A[i, i] == 0:
            # Szukamy wiersza do zamiany
            for j in range(i + 1, n):
                if A[j, i] != 0:
                    swap_rows(A, i, j)
                    swap_rows(b, i, j)
                    swap_rows(memory, i, j)
                    break
            else:
                # Jeśli nie znaleziono wiersza, próbujemy zamianę kolumn
                for j in range(i + 1, n):
                    if A[i, j] != 0:
                        swap_columns(A, i, j)
                        break
                else:
                    raise ValueError("Nie można uniknąć zera na przekątnej!")

    return A, b


def jordan_elimination(A, b, memory):
    """
    Rozwiązuje układ równań liniowych Ax = b metodą eliminacji Jordana-Gaussa.
    :param memory:
    :param A: macierz współczynników (n x n)
    :param b: wektor wynikowy (n x 1)
    :return: wektor rozwiązań x (n x 1)
    """
    A, b = fix_diagonal_zeros(A, b, memory)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    AB = np.hstack((A, b))  # Tworzymy rozszerzoną macierz
    n = len(b)

    for i in range(n):
        A, b = fix_diagonal_zeros(A, b, memory)  # Sprawdzamy przekątną po każdej eliminacji

        # Normalizacja wiersza
        AB[i] /= AB[i, i]

        # Eliminacja we wszystkich innych wierszach
        for j in range(n):
            if i != j:
                AB[j] -= AB[i] * AB[j, i]

    return AB[:, -1]  # Zwracamy ostatnią kolumnę (rozwiązanie)