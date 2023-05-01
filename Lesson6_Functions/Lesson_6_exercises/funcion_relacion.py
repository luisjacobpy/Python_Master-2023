"""
Realiza una función llamada relación () que apartir de dos números cumpla lo siguiente:

* Si el primer numero es mayor que el segundo, devolver 1 
* Si el primer numero es menor que el segundo, devolver -1
* Si el ambos numeros son iguales devolver 0
"""
def relacion(valor1, valor2):
    if valor1 > valor2:
        return 1
    elif valor1 < valor2:
        return -1
    elif valor1 == valor2:
        return 0


# Build objects
"""
Asignmo el resultado de la llamada de la funcion a una variable
Despues cisualizo en consola el resultado

"""
result_1 = relacion(5,10)
print(result_1)

print(relacion(10,5))

    