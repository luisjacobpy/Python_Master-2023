# Importamos el modulo
import math 
PI = math.pi # Asignamos el valor a la variable
print(PI)

"""
Fuhncion para obtener el area de un circulo
"""
def area_circulo(radio):
    return (radio**2) * PI

circulo_1 = area_circulo(5)
print(circulo_1)