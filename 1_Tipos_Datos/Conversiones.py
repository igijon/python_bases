# implícitas

num1 = 20
num2 = 30.5

print(type(num1), type(num2))

num1 = num1 + num2

print(type(num1), type(num2))

# explícitas
num1 = 5.8
print(num1, type(num1))

num2 = int(num1)
print(num2, type(num2))

edad = input("Dime tu edad: ")

print(type(edad))

edad = int(edad)

print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad, type(nueva_edad))
print("Tu nueva edad va a ser "+str(nueva_edad))
