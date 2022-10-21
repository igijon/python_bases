class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('El animal ha nacido')

    def hablar(self):
        print('El animal emite un sonido')


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super(Pajaro, self).__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pájaro vuela {metros} metros')


print(Animal.__subclasses__())  # Me indica las clases que heredan de él
print(Pajaro.__bases__)  # Me indica el padre

mi_animal = Animal(3, 'azul')
piolin = Pajaro(2, 'verde', 10)
piolin.hablar()
piolin.volar(100)



