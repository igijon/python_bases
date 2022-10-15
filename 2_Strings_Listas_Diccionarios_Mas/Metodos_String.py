texto = "Este es el texto de prueba"
resultado = texto
print(resultado)

resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

f = "-".join([a, b, c, d])
print(f)

resultado = texto.find("s")  # Similar pero si el carácter no existe, no falla... da -1
print(resultado)

resultado = texto.find("texto")
print(resultado)

resultado = texto.replace("prueba", "ejemplo")
print(resultado)

resultado = texto.replace("r", "x")
print(resultado)
