archivo = open('prueba.txt', 'w')  # Si omitimos el modo de apertura lo abre en modo sólo lectura
# Sobreescribe el fichero anterior. Si no existe el fichero, lo crea
archivo.write('soy el nuevo texto')
archivo.write('si no añado \n no agrega una nueva línea')
archivo.write('''Ahora sí escribe saltos
de línea y          tabuladores''')
lista = ['Esto es una línea', 'Esto es otra línea', 'Tercera línea']
archivo.writelines(lista)
# Toma distintas cadenas pero no las escribe en líneas distintas, las escribe una a continuación de otra

for p in lista:
    archivo.writelines(p+'\n')

archivo.close()

archivo = open('prueba.txt', 'a')  # abre el archivo y pone el cursor al final para añadir
archivo.write('Bienvenido')
archivo.close()
