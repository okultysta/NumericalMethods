from zad_2.algorithm import jordan_elimination

A = [[3,3,1],
     [2,5,7],
     [1,2,1]]

B = [12,33,8]

memory = ["x1", "x2", "x3"]

x = jordan_elimination(A, B, memory)
print(memory, x)