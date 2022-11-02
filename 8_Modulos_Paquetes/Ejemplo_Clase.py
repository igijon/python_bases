class Prueba:
    def __init__(self, elem: int):
        self._elem = elem

    def metodo_prueba(self, objeto: 'Prueba'):
        print(str(objeto) + str(self._elem))

    def __str__(self):
        return str(self._elem)


class Prueba2:
    def __init__(self, elem: int):
        self._elem = elem

    def metodo_prueba2(self, objeto: Prueba):
        print(objeto + self._elem)


mi_prueba = Prueba(3)
print(mi_prueba)
mi_prueba2 = Prueba(2)
mi_prueba.metodo_prueba(mi_prueba2)
