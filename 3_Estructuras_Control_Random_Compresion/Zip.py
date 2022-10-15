nombres = ['Enrique', 'Abraham', 'Alonso']
edades = [65, 34, 42]
ciudades = ['Madrid', 'Córdoba', 'Sevilla']
combinados = list(zip(nombres, edades))  # Si no le hago un cast no puedo ver su contenido
print(combinados)

edades.append(45)
combinados = list(zip(nombres, edades))
print(combinados)  # Llega al máximo de la longitud de la lista más corta

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
