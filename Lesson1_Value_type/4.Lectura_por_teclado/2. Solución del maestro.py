# Leemos el nombre y el apellido en dos variables
nombre = input()
apellido = input()
 
# Leemos la edad y la transformamos a número entero
edad = int(input())
 
# Leemos un número y lo transformamos a flotante para usarlo de número mágico
numero_magico = float(input())
 
# Generamos la cadena final sumando la porción calculada en forma de cadena
cadena_final = nombre +" "+ apellido +": Tu número de la suerte es el "+str(edad*numero_magico)
