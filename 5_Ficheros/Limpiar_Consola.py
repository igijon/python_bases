from os import system

nombre = input("Nombre: ")
edad = input("Edad: ")
system('clear')  # Si usas windows 'cls'
# Para que funcione en Pycharm => Run -> Debug -> Edit configuration -> Execution. Emulate terminal in output console
print(f"Tu nombre es {nombre} y tienes {edad} años")


