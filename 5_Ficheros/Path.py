from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
# Permite como elementos cadenas y otros Paths y los compone correctamente

guia2 = guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)

print(guia.parent)  # Devuelve el antecesor más inmediato
print(guia.parent.parent)

# Si quiero ver todos los ficheros txt que haya en Europa
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)

# Para que incluya todas las carpetas y subcarpetas que vaya encontrando podemos hacer
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)