mi_lista = [2, 2, 2, 2, 2, 2, 2]
print(len(mi_lista))
print(mi_lista)


class Objeto:
    pass


mi_objeto = Objeto()
# print(len(mi_objeto)) Dará error
print(mi_objeto)  # Representación en un string de mi objeto básico


class Album:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        # Siempre lo va a borrar pero además hemos implementado que informe
        print(f'Se ha borrado la instancia de album')

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor

    # También podemos añadir como métodos especiales __add__ y __sub__ por ejemplo


mi_album = Album('Robe Iniesta', 'Bienvenidos al temporal', 19)
print(mi_album)
print(len(mi_album))

del mi_album

print(mi_album)  # Da error porque he borrado la instancia
