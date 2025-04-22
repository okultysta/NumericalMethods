import numpy as np

def swap_rows(A, row1, row2):
    A[[row1, row2]] = A[[row2, row1]]

def swap_columns(A, col1, col2):
    A[:, [col1, col2]] = A[:, [col2, col1]]


def fix_diagonal_zeros(AB, memory):
    n = AB.shape[0]  # Liczba równań (i zmiennych)

    for i in range(n):
        if AB[i, i] == 0:
            # Szukamy wiersza do zamiany
            for j in range(i + 1, n):
                if AB[j, i] != 0:
                    swap_rows(AB, i, j)
                    break
            else:
                # Jeśli nie znaleziono wiersza, próbujemy zamianę kolumn
                for j in range(i + 1, n):
                    if AB[i, j] != 0:
                        swap_columns(AB, i, j)
                        memory[i], memory[j] = memory[j], memory[i]  # Aktualizujemy nazwy zmiennych
                        break
                else:
                    raise ValueError("Nie można uniknąć zera na przekątnej! Układ może być nieoznaczony lub sprzeczny.")

    return AB, memory


def jordan_elimination(A, b, memory):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    AB = np.hstack((A, b))  # Tworzymy rozszerzoną macierz
    n = len(b)
    #print(AB)
    #print()

    for i in range(n):
        AB, memory = fix_diagonal_zeros(AB, memory)  # Sprawdzamy przekątną po każdej eliminacji
        #print(AB)
        #print()
        # Normalizacja wiersza
        AB[i] /= AB[i, i]

        # Eliminacja we wszystkich innych wierszach
        for j in range(n):
            if i != j:
                AB[j] -= AB[i] * AB[j, i]

    #print(AB)
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
