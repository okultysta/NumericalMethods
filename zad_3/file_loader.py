def load_from_file(filename):
    filename = "../pliki_zad3/" + filename
    with open(filename, 'r') as file:
        line = file.readline()
        numbers = line.strip().split()
        nodes = [float(num) for num in numbers]
    return nodes