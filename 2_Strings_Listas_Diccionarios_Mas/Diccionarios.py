diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
print(type(diccionario))

resultado = diccionario['c1']
print(resultado)

cliente = {
    'nombre': 'Juan',
    'apellido': 'González',
    'edad': 56,
    'peso': 75,
    'talla': 1.76
}

consulta = cliente['apellido']
print(consulta)


dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic = {1: 'a', 2: 'b'}
print(dic)
dic[3] = 'c'
print(dic)
dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())

print(dic.items())
