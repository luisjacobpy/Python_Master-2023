"""
Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se blobee y ademas esplica en un mensaje al usuario la causa y/o solucion


codigo 
resultado = 10/0
"""

# Detectosmos el codigo tendiente a errorres dentro del 'try'

try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: No es posible dicvidir por cero, debes introducir un numero distinto")
