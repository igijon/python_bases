from colored import fg, bg, attr

color = fg(1) + bg(15)
print(color + "hola Mundo" + attr(0))
