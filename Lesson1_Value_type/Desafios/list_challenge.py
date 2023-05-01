""""
La siguiente matriz (con listas anidadas) debe cumplir una condicion, y es que en cada fila
el cuarto elemento siempre debe ser el resultado de sumar los tres primeros

Ultiliza slicing para corregir
sum(list) deveulve una suma de todos los elementos de la lista.

"""
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
print(matriz)
# Desarrollo
# Segunda lista
matriz[1][-1] = sum( matriz[1][:-1]) # Hacer la suma de los tres primeros // Hemos cambiado el 7 por un 6
print(matriz)
#Ultima lista
matriz[-1][-1] = sum( matriz[-1][:-1])
print(matriz)
