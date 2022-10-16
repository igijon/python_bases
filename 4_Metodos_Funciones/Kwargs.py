def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total


resultado = suma(x=3, y=5, z=2)
print(resultado)


def prueba(num1, num2, *args, **kwargs):  # el orden no es casual
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


prueba(15, 46, 233, 'hola', 45, 34, x='palabra1', y=34, z='argumento final')

args = [200, 300, 400, 500]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}
prueba(15, 30, args, kwargs)
prueba(15, 30, args, **kwargs)

