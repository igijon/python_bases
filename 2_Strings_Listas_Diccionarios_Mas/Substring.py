texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2:5]  # Va desde el índice 2 hasta el 5 sin incluir
print(fragmento)

fragmento = texto[2:]
print(fragmento)

fragmento = texto[:5]
print(fragmento)

fragmento = texto[2:10:2]  # Extraerá cada dos caracteres
print(fragmento)

fragmento = texto[::3]
print(fragmento)

fragmento = texto[::-1]  # Obtenemos la cadena al revés
print(fragmento)



