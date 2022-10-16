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

resultado = check_3_cifras2([2, 34, 567, 67, 678])
print(resultado)

precios_cafe = [('capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''

    for c, p in lista_precios:
        if p > precio_mayor:
            precio_mayor = p
            cafe_caro = c

    return cafe_caro, precio_mayor


cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe} cuyo precio es {precio}')
