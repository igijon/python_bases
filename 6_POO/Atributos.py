class Pajaro:

    # Atributos de clase
    alas = True

    # Constructor
    def __init__(self, color, especie):
        # Atributos de instancia
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro', 'Tucán')
print(f"Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")
print(Pajaro.alas)
print(mi_pajaro.alas)


