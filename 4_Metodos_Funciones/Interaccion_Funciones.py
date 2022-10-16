from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)


# Comprobar intento
def check_intento(lista, intento):
    if lista[intento-1] == ['-']:
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f"Te ha tocado {lista[intento-1]}")


# Interacción entre funciones
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
check_intento(palitos_mezclados, seleccion)
