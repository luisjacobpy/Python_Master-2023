""""
Condiciones
Utilizando una condición if-elif-else debes realizar un programa que compare la longitud de dos variables (cadena_1 y cadena_2) y en función del resultado almacene un valor en otra variable llamada resultado:

Si cadena_1 es más larga que cadena_2 la variable resultado deberá tener el valor entero 1.

Si cadena_1 es más corta que cadena_2 la variable resultado deberá tener el valor entero 2.

Si cadena_1 tiene la misma longitud que cadena_2 la variable resultado deberá tener el valor entero 0.

Notas:

Las variables cadena_1 y cadena_2 se importan de otro fichero y no puedes editarlas.
"""

if cadena_1 > cadena_2:
    resultado = int(1)
elif cadena_2 > cadena_1:
    resultado = int(2)
else:
    resultado = int(0)
    
# Teache's solution
# Variables del ejercicio (no las edites)
from evaluate import cadena_1, cadena_2

# Comprobamos si la longitud de la cadena1 es mayor que cadena2
if len(cadena_1) > len(cadena_2):
    # En ese caso el resultado será 1
    resultado = 1
# Por contra si la longitud de cadena1 es menor que cadena2
elif len(cadena_1) < len(cadena_2):
    # El resultado será 2
    resultado = 2
# En cualquier otro caso el resultado será 0
else:
    resultado = 0
