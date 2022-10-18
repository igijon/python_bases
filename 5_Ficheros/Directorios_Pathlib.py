from pathlib import Path, PureWindowsPath

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

ruta = Path('../recursos/otro_ejemplo.txt')
print(ruta.read_text())  # No hemos tenido que abrir ni cerrar nuestro fichero
print(ruta.name)  # Nombre del fichero
print(ruta.suffix)
print(ruta.stem)

ruta_windows = PureWindowsPath(ruta)
print(ruta_windows)

if not ruta.exists():
    print('Este archivo no existe')
else:
    print('Genial! Existe')



