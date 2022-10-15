monedas = 5
while monedas > 0:
    print(f"Tengo {monedas}  monedas")
    monedas -= 1
else:
    print("No tengo más dinero")  # esto lo ejecuta al salir y no es necesario

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres seguir (s/n)?: ')
else:
    print("Gracias")

respuesta = 's'
while respuesta != 's':
    pass  # Como programador, puedo poner pass hasta que implemente este bloque porque necesita 1 instrucción.
else:
    print("Gracias")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'n':
        break
    print(letra)


nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'n':
        continue
    print(letra)


