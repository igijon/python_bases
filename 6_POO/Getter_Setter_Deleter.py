class Circulo:

    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError('Radio debe ser positivo')

    @radio.deleter
    def radio(self):
        del self._radio


c1 = Circulo(3)
print(c1.radio)
c1.radio = 4
# c1.radio = -1 Esto lanza una excepción
del c1.radio
print(c1.radio)
