# Coincidencias de patrones estructurales
serie = "N-01"
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

actor = {
    'nombre': 'Alicia Wilkander',
    'edad': 34,
    'pais_nacimiento': 'Suecia'
}
pelicula = {
    'titulo': 'Ex machina',
    'ficha_tecnica': {'anio': 2014, 'director': 'Alex Garland', 'genero': 'Ciencia ficción'}
}

el = [actor, pelicula, 'Sorpresa']
for e in el:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'pais_nacimiento': pais_nacimiento}:
            print(f'Actriz: {nombre} con {edad} años y cuyo país de nacimiento es {pais_nacimiento}')
        case {'titulo': titulo,
              'ficha_tecnica': {'anio': anio, 'director': director, 'genero': genero}}:
            print(f'Película: {titulo}, Año: {anio}, Director: {director}, Género: {genero}')
        case _:
            print(f'Elemento distinto: {e}')
