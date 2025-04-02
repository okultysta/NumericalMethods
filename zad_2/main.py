import algorithm
from zad_2.file_loader import load_from_file
"""
A = [[3,3,1],
     [2,5,7],
     [1,2,1]]

B = [12,33,8]

memory = ["x1", "x2", "x3"]

x, memory = algorithm.jordan_elimination(A, B, memory)
print(memory, x)
"""

#"""
filename = input("Podaj nazwę pliku z układem równań: ")
A, b, memory = load_from_file(filename)

if algorithm.is_inconsistent(A, b):
     print("Układ jest sprzeczny.")
elif algorithm.is_underdetermined(A, b):
     print("Układ jest nieoznaczony (nieskończenie wiele rozwiązań).")
else:
     x, memory = algorithm.jordan_elimination(A, b, memory)
     print("Rozwiązanie:")
     for var, val in zip(memory, x):
          print(f"{var} = {val:.3f}")
#"""