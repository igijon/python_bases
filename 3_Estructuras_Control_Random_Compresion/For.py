lista = ['a', 'b', 'c']
for letra in lista:
    numero_letra = lista.index(letra)
    print(f"La letra {numero_letra+1} es {letra}")

lista = ['pablo', 'laura', 'alonso', 'inma']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con l')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for n in numeros:
    mi_valor += n  # Acumulador

print(mi_valor)

palabra = 'python es genial'
for letra in palabra:
    print(letra)

for elem in (1, 2, 3):
    print(elem)

for x, y in [[1, 2], [3, 4], [5, 6]]:
    print(x, y)

dic = {'c1': 'a', 'c2': 'b', 'c3': 'c'}
for item in dic:
    print(item)  # Imprime sólo las claves

for clave, valor in dic.items():
    print(clave, valor)

for value in dic.values():
    print(value)

for key in dic.keys():
    print(key)
