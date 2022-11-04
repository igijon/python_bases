from datetime import datetime, date

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(mi_fecha)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)
vida = defuncion-nacimiento
print(vida.days)

despierta = datetime(2022,10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme-despierta
print(vigilia)
print(vigilia.seconds)


