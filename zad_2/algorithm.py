import numpy as np

def swap_rows(A, row1, row2):
    A[[row1, row2]] = A[[row2, row1]]

def swap_columns(A, col1, col2):
    A[:, [col1, col2]] = A[:, [col2, col1]]


def fix_diagonal_zeros(A, b, memory):
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

    return A, b, memory


def jordan_elimination(A, b, memory):
    A, b, memory = fix_diagonal_zeros(A, b, memory)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    AB = np.hstack((A, b))  # Tworzymy rozszerzoną macierz
    n = len(b)

    for i in range(n):
        A, b, memory = fix_diagonal_zeros(A, b, memory)  # Sprawdzamy przekątną po każdej eliminacji

        # Normalizacja wiersza
        AB[i] /= AB[i, i]

        # Eliminacja we wszystkich innych wierszach
        for j in range(n):
            if i != j:
                AB[j] -= AB[i] * AB[j, i]

    return AB[:, -1], memory  # Zwracamy ostatnią kolumnę (rozwiązanie)


def is_inconsistent(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    AB = np.hstack((A, b))  # Macierz rozszerzona

    rank_A = np.linalg.matrix_rank(A)
    rank_AB = np.linalg.matrix_rank(AB)

    return rank_A != rank_AB


def is_underdetermined(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    AB = np.hstack((A, b))  # Macierz rozszerzona

    rank_A = np.linalg.matrix_rank(A)
    rank_AB = np.linalg.matrix_rank(AB)

    return rank_A == rank_AB and rank_A < len(A)
