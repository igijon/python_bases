class Alumno:
    def __init__(self, nombre=''):
        self.nombre = nombre
        self._secreto = 'asdasd'
        self.__secreto1 = 'secretillo'


a1 = Alumno('Jose')
print(a1.nombre)
print(a1._secreto)
print(a1._Alumno__secreto1)
print(a1.__secreto1)



