

def bisection_iteration(a, b, function, iterations):
    if function(a) * function(b)>=0:
        raise ValueError("Wartosci funkcji musza miec rozne znaki")
    x = (a+b)/2
    old_x = x
    for i in range(iterations):
        old_x = x
        x = (a+b)/2
        if function(x) == 0:
            return x, abs(x - old_x)
        elif function(x)*function(a)<0:
            b=x
        else:
            a=x
    return x, abs(x - old_x)

def bisection_epsilon(a,b,function,epsilon):
    if function(a) * function(b)>=0:
        raise ValueError("Wartosci funkcji musza miec rozne znaki")
    x = (a+b)/2
    old_x = a
    iterations = 1
    while abs(x - old_x) > epsilon:
        if function(x) == 0:
            return x, iterations
        elif function(x)*function(a)<0:
            b=x
        else:
            a=x
        old_x = x
        x = (a + b) / 2
        iterations += 1
    return x, iterations
