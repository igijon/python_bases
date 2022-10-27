isNumber = False
while not isNumber:
    try:
        x = int(input("Introduce un número: "))
        isNumber = True
    except ValueError:
        print('Debes introducir un número')
print(x)

cad = 0
try:
    print(10/int(cad))
except ValueError:
    print('No se puede convertir a entero')
except ZeroDivisionError:
    print('No se puede dividir por cero')
except:
    print('Otro error')
finally:
    print('Terminamos el programa')

cad = 'a'
try:
    i = int(cad)
except ValueError as error:
    print(type(error))
    print(error.args)
    print(error)
