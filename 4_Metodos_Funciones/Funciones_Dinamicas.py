def check_3_cifras(numero):
    return numero in range(100, 1000)


def check_3_cifras2(lista):
    num_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            num_3_cifras.append(n)
    return num_3_cifras


resultado = check_3_cifras(345)
print(resultado)

resultado = check_3_cifras2([2,34,567,67,678])
print(resultado)