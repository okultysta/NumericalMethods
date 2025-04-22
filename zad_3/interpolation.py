import math

def lagrange_interpolation(nodes, func):
    y_values = [func(x) for x in nodes]

    def L(x):
        result = 0
        n = len(nodes)
        for i in range(n):
            xi, yi = nodes[i], y_values[i]
            li = 1
            for j in range(n):
                if j != i:
                    li *= (x - nodes[j]) / (xi - nodes[j])
            result += yi * li
        return result

    return L
