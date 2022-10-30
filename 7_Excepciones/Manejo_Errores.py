def suma():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1+n2)
    print('Gracias por sumar '+n1+' y '+n2)


try:
    suma()
except TypeError:
    print('Ha ocurrido un error de tipo')
except ValueError:
    print('Se ha introducido un carácter no numérico')
else:
    print('Hiciste todo bien')
finally:
    print('Hemos terminado')