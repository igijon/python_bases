palabra = "python"
lista = [letra for letra in palabra]

# for letra in palabra:
#    lista.append(letra)

print(lista)

lista = [n/2 for n in range(0, 21, 2)]
print(lista)

lista = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista)

# El coste de esto es la legibilidad pero es muy eficiente

pulgadas = [10, 20, 30, 40, 50]
centimetros = [p*2.54 for p in pulgadas]
print(f'Pulgadas: {pulgadas}')
print(f'Centimetros: {centimetros}')
