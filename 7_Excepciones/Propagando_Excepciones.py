def dividir(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        raise


def nivel(numero):
    if numero<0:
        raise ValueError('El úmero debe ser positivo: '+str(numero))
    else:
        return numero


x = 5
y = 0
try:
    dividir(x, y)
except Exception as error:
    print(error)
