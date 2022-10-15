x = False
if x:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'tardígrado'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé qué animal tienes')

edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion > 7:
        print('Aprobado')
else:
    print('Eres adulto')
