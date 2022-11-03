from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [8,6,9,5,4,5,5,5,5,5,5,6,5,7,3]
print(Counter(numeros))
print(Counter('mississippi'))
frase = 'Al pan pan y al vino vino'
print(Counter(frase))
print(Counter(frase.split()))

serie = Counter([2,2,2,2,2,2,2,24,56,356,2,2,1,3])
print(serie.most_common())
print(serie.most_common(1))  # Muestra el número que más se repite
print(list(serie))

mi_dict = {'uno': 'verde',
           'dos': 'azul',
           'tres': 'rojo'}
print(mi_dict['uno'])

mi_dict = defaultdict(lambda: 'nada')
print(mi_dict['cuatro'])

mi_tupla = (500, 18, 65)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)
print(ariel[2])

