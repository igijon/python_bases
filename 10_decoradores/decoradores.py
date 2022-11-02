def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula


operacion = cambiar_letras('may')
operacion('palabra')


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adiós')
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


minusculas('Python')
mayusculas('Python')

minusculas_decorada = decorar_saludo(minusculas)
minusculas_decorada('Prueba')
