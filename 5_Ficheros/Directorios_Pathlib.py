from pathlib import Path

"""
Este modo no nos asegura que funcione en distintos SSOO
archivo = open('../recursos/otro_archivo.txt', 'r')
print(archivo.read())
archivo.close()"""

carpeta = Path('../recursos')
# Cualquier sistema que abra esto lo podrá leer
archivo = carpeta / 'otro_ejemplo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()
