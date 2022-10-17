import os

ruta = os.getcwd()  # Obtiene el pwd
print(ruta)
os.chdir('../recursos')
ruta = os.getcwd()
archivo = open('otro_ejemplo.txt', 'r')
print(archivo.read())
archivo.close()


os.makedirs('otro_directorio')
os.chdir('otro_directorio')
ruta = os.getcwd()+'/prueba_nueva.txt'
print(ruta)

elemento = os.path.basename(ruta)
print(elemento)  # Nombre de base del fichero
elemento = os.path.dirname(ruta)
print(elemento)  # Primera parte de nuestra ruta
elementos = os.path.split(ruta)
print(elementos)

os.rmdir(elementos[0])

