import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al día"

print('ayuda' in texto)
patron = 'nada'

busqueda = re.search(patron, texto)
print(busqueda)
patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())  # Ubicación
print(busqueda.start())
print(busqueda.end())
busqueda = re.findall(patron, texto)
print(len(busqueda))
for elem in re.finditer(patron, texto):
    print(elem.span())

texto = 'Llama al 564-525-6588 ahora mismo o el lunes'
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)

print(resultado)

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
print(resultado.group())
print(resultado.group(1))

# Clave que empiece con una letra y tenga 8 caracteres, los 7 restantes alfanuméricos
clave = input('Clave: ')
patron = r'^\D{1}\w{7}$'
busqueda = re.search(patron, clave)
print(busqueda)
busqueda = re.search(r'lunes|martes', texto)
print(busqueda)
busqueda = re.search(r'...smo', texto)
print(busqueda)
busqueda = re.search(r'^\D', texto)
print(busqueda)
busqueda = re.findall(r'[^\s]', texto)
print(busqueda)
busqueda = re.findall(r'[^\s]+', texto)
print(busqueda)
print(''.join(busqueda))
