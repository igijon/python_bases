class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('El animal ha nacido')


class Pajaro(Animal):
    pass


print(Animal.__subclasses__())  # Me indica las clases que heredan de él
print(Pajaro.__bases__)  # Me indica el padre

piolin = Pajaro(2, 'verde')
piolin.nacer()  # Lo ha heredado
print(piolin.color)

