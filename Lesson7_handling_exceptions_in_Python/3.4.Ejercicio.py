"""
Excepciones
Tomando la solución al anterior ejercicio, en lugar de devolver None al dividir entre cero, debes capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje No se puede dividir entre cero si falla el código.
"""
\
def dividir(a, b):
    try:
        return a/b
        
    except:
        print("No se puede dividir entre cero")