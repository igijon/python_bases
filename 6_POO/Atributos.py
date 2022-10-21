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


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(10)
