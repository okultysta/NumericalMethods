def load_from_file(filename):
    filename = "../pliki_zad2/" + filename
    with open(filename, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    A = []
    b = []
    memory = [f"x{i+1}" for i in range(n)]

    for line in lines[1:n + 1]:
        values = list(map(float, line.strip().split()))
        A.append(values[:-1])
        b.append(values[-1])

    return A, b, memory