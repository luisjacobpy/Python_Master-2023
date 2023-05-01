"""
Instrucción llamada input

"""

# valor = int(input("Introduce un numero entero: "))
# valor = float(valor)
# print(valor+10)

# Completa el ejercicio


"""
Realiza un programa con los siguientes requisitos:

Debes leer por teclado dos cadenas de caracteres, una llamada nombre y otra llamada apellido.

Debes leer por teclado un número entero llamado edad (recuerda que la variable debe ser de tipo entero).

Debes leer por teclado un número flotante llamado numero_magico.

Finalmente debes crear una variable cadena_final con el siguiente formato:

NOMBRE APELLIDO: Tu número de la suerte es el EDAD*NUMERO_MAGICO
Por ejemplo, si se introducen los valores "Juan", "Pérez", 20 y 4.5 , cadena_final contendrá lo siguiente:

Juan Pérez: Tu número de la suerte es el 90.0
Nota: En este ejercicio no tienes que intoducir ningún valor en los inputs, sólo programar correctamente las variables y generar la cadena_final tal como se pide. El sistema se encargará de introducir él mismo los valores en los inputs y comprobar que el resultado sea el esperado. Si lo

"""

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
edad = float(edad)
numero_magico = float(input(("Numero magico: ")))
cadena_final = f"{nombre} {apellido}: Tu número de la suerte es el {float(edad * numero_magico)}"
print(cadena_final)
