mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[-4]
print(resultado)

resultado = mi_texto.index("n")
print(resultado)

resultado = mi_texto.index("x")
print(resultado)

resultado = mi_texto.index("a")
print(resultado)  # Me da la primera ocurrencia de izquierda a derecha

resultado = mi_texto.index("a", 5, 12)  # Busco desde el índice 5 hasta el índice 11 incluído
print(resultado)

resultado = mi_texto.rindex("a")  # Busca de derecha a izquierda
print(resultado)





