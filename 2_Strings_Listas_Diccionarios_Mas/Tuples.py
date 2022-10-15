mi_tuple = 1, 2, 3, 4
print(mi_tuple)

mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple))

print(mi_tuple[0])
print(mi_tuple[-2])

# Son inmutables, así que no podemos cambiar un elemento del tuple

mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2][0])
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
print(mi_tuple)

mi_tuple = tuple(mi_tuple)
print(mi_tuple)
print(type(mi_tuple))

t = (1, 2, 3, 1)
x, y, z, a = t  # Esto también se puede hacer con listas y diccionarios pero tiene que coincidir el número
print(x, y, z, a)

print(len(t))
print(t.index(3))
print(t.count(1))

