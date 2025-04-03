import algorithm
from zad_2.file_loader import load_from_file

running = True
while running:
     filename = input("Podaj nazwę pliku z układem równań: ")
     A, b, memory = load_from_file(filename)

     print()
     print("Wczytany układ:")
     for i, row in enumerate(A):
          row_str = " + ".join(f"{coef}*{memory[j]}" for j, coef in enumerate(row))
          print(f"{row_str} = {b[i]}")

     if algorithm.is_inconsistent(A, b):
          print()
          print("Układ jest sprzeczny.")
     elif algorithm.is_underdetermined(A, b):
          print()
          print("Układ jest nieoznaczony (nieskończenie wiele rozwiązań).")
     else:
          x, memory = algorithm.jordan_elimination(A, b, memory)
          print()
          print("Rozwiązanie:")
          for var, val in zip(memory, x):
               print(f"{var} = {val:.3f}")
     
     flag = True
     while flag:
          print()
          answear = input("Czy chcesz wczytać kolejny układ? [Y/N]: ")
          if answear == "N" or answear == "n":
               running = False
               flag = False
               print("Program zakończony")
          elif answear == "Y" or answear == "y":
               flag = False
          else:
               print("Nieznana opcja. Spróbuj ponownie.")

#problem w 7 i 5