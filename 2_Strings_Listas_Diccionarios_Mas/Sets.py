# Son elementos únicos, no contienen repeticiones, si añadimos una la ignora
mi_set = set([1, 2, 3, 4, 4, 4, 4])  # Debemos poner los elementos o bien en una lista o bien en una tupla... con algún
# tipo de llave.
print(mi_set)
print(type(mi_set))

otro_set = {1, 2, 3}
print(type(otro_set))
print(otro_set)

# print(mi_set[0])  # Esto falla porque no son indexables

# Dentro de un set no puedo poner listas ni diccionarios, sí tuples porque son inmutables.

print(len(mi_set))
print(2 in mi_set)  # también se puede hacer en los diccionarios si lo que buscamos es la clave

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.add(2)
print(s1)
s1.remove(3)  # Si no lo tiene da error
print(s1)
s1.discard(3)  # Si no lo tiene, no pasa nada... no hace nada
elemento_eliminado = s1.pop()  # Elimina un elemento aleatoriamente
print(elemento_eliminado)
s1.clear()  # Borra todos los elementos del conjunto
print(s1)
