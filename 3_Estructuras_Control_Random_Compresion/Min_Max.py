menor = min(58, 96, 64, 35)
mayor = max(58, 96, 64, 35)

print(menor, max)

lista = [58, 96, 64, 35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['Enrique', 'Fernando', 'Chad', 'Abraham', 'Alonso']
print(min(nombres))

nombre = 'Carlos'
print(min(nombre))
nombre = nombre.lower()
print(min(nombre))

dic = {'c1': 45, 'c2': 11}
print(min(dic))  # Ordena por defecto las claves
print(min(dic.values()))
