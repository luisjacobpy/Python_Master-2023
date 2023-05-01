"""
Index error

"""

lista = [1, 2, 3, 4, 5]

try:
    lista[10]
except IndexError:
    print(f"Error: el indice al que intentas acceder se encuentra fuera de rango la longgitud de la lista es:{len(lista)}")
    