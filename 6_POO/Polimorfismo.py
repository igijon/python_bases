class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+' dice muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+' dice bee')


vaca = Vaca('Aurora')
oveja = Oveja('Luisa')

vaca.hablar()
oveja.hablar()

animales = [vaca, oveja]

'''La lista tiene tiene objetos distintos y llama al método en
función del tipo de objeto que sea'''
for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca)
animal_habla(oveja)