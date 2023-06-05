"""
Realiza un programa que lea dos numeros por teclado y permita elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos numeros
- Mostrar una resta de los dos números
- Mosdstrar una multipliocación de los dos dumeros.
En caso de no introducir una opción válida, el programa informará que no es correcta.

"""
# Definimos las variables que se introducen por teclado
FIRST_NUMBER = (float(input("Please, introduce the first number: ")))
SECOND_NUMBER = (float(input("Please, introduce the second number: ")))

# Definimos las variables de opciones
# We build the option of variables
print(
"""
Selecciona la opción que deseas:
a) Mostrar una suma de los dos numeros
b) Mostrar una resta de los dos números
c) Mosdstrar una multipliocación de los dos dumeros.
"""
)
option = False
while option == False:

    opcion = str(input("Introduce el indice la de opción seleccionadoa, ejemplo: a, b, c: "))

    if opcion == "a":
        print(f"El resultado de la suma de {FIRST_NUMBER} + {SECOND_NUMBER} es:", FIRST_NUMBER + SECOND_NUMBER)
        option = True
    elif opcion == "b":
        print(f"El resultado de la resta de {FIRST_NUMBER} - {SECOND_NUMBER} es:", FIRST_NUMBER - SECOND_NUMBER)
        option = True
    elif opcion == "c":
        option = True
        print(f"El resultado de la multipicación de {FIRST_NUMBER} * {SECOND_NUMBER} es:", FIRST_NUMBER * SECOND_NUMBER)

    else:
        print("Valor no válido")
        option = False
