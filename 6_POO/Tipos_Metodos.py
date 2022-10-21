class Pajaro:

    # Atributos de clase
    alas = True

    # Constructor
    def __init__(self, color, especie):
        # Atributos de instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pío pío, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'

    @classmethod
    def poner_huevos(cls, cantidad_huevos):
        print(f'Puso {cantidad_huevos} huevos')
        cls.alas = False


    @staticmethod
    def mirar():
        """No puedo cambiar los atributos de instancia ni de clase
        Podemos usar para métodos qu eno queremos que modifiquen objetos de la instancia ni de la
        clase.
        Estos métodos no dependen de la clase pero están ligados de algún modo a ella"""
        print("El pájaro mira")


piolin = Pajaro('amarillo', 'canario')
print(piolin.color)
piolin.pintar_negro()
print(piolin.color)
piolin.volar(5)

# Imaginamos que no tenemos ninguna instancia...
Pajaro.poner_huevos(3)  # Estos métodos no pueden acceder a los atributos de instancia
# Pajaro.piar()  # Dará un error
print(Pajaro.alas)
