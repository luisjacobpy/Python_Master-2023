imprimir = print
imprimir("Welcome to the interactive menu")
while(True):
    print("""What do you want to do? write an option
    1) Greet
    2) Adding two numbers
    3) Go out / Close the program
    """)
# Input information
    opcion = input()
    if opcion == "1":
        print("Hello every one!")
    elif opcion == "2":
        n1 = float(input("Introduce the first number to add: "))
        n2 = float(input("Introduce the second number to add: "))
        print("The result of the adding is:", (n1+n2))
    elif opcion == "3":
        print("See you later!")
        break # Important, the reason I wan't infinite cicle
    else:
        print("Invalid command, Try again!")


"""
Bucle while
Realiza un programa que lea un número por teclado y lo almacene en una variable llamada numero.

Si ese número introducido por teclado no es múltiple de 5 debe repetirse de nuevo la lectura hasta que lo sea.

Notas:

Debes asegurarte de que la variable numero es un número entero introducido con la instrucción input.

Si intentas asignar un múltiple de 5 manualmente a la variable numero la solución fallará

"""
# Completa el ejercicio
numero = -1

# Mientras el numero no sea múltiple de 5
while numero % 5 != 0:
    # Volveremos a leer un número por teclado y lo almacenaremos transformándolo a entero
    numero = int(input())
