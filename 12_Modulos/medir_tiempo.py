import time
import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1 ):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
print(prueba_for(15))
final = time.time()
print(final-inicio)
inicio = time.time()
print(prueba_while(15))
final = time.time()
print(final-inicio)

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1 ):
        lista.append(num)
    return lista
'''
# number nos indica el número de veces que lo prueba para generar el tiempo
duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion)

declaracion2 = '''
prueba_while(10)
'''
mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(duracion2)
