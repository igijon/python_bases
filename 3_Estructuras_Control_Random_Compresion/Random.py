from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 50), 2)  # Esta vez me devuelve un decimal que puedo redondear
print(aleatorio)

aleatorio = random()  # Fracción de un entero (aleatorio entre 0 y 1)
print(aleatorio)

colores = ['rojo', 'verde', 'azul', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)  # Podría servirnos por ejemplo en un juego de cartas
print(numeros)
