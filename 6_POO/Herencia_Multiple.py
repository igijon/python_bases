class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print('qué tal?')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
"""Coge el método del que hereda primero, porque hay un orden
de búsqueda hacia arriba"""
mi_nieto.reir()

# Así puedo ver el orden en el que se resuelven los métodos en la herenciate
print(Nieto.__mro__)

