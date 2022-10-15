mi_lista = ['a', 'b', 'c', 'd']
otra_lista = ['hola', 55, 6.1]
resultado = len(mi_lista)
print(type(mi_lista))
print(resultado)

resultado = mi_lista[0:]
print(resultado)

mi_lista2 = ['d', 'e', 'f']
print(mi_lista+mi_lista2)  # Crea una lista nueva
mi_lista3 = mi_lista+mi_lista2
print(mi_lista3)

mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)

elemento_eliminado = mi_lista3.pop()  # Por defecto elimina el último de sus elementos.
print(mi_lista3)
print(elemento_eliminado)

elemento_eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(elemento_eliminado)

lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()  # No devuelve nada
print(lista)

lista.reverse()
print(lista)
