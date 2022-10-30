def suma():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1+n2)
    print('Gracias por sumar')

try:
    suma()
except:
    print('Algo no ha salido bien')
else:
    print('Hiciste todo bien')
finally:
    print('Hemos terminado')