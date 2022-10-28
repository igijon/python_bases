class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'Hola, me llamo {self.nombre}')


class Anuales(Cliente):
    pass