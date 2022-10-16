def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(5, 6, 5, 7, 89))
