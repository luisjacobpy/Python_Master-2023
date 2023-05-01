"""
Funcion que recibe un valor, si el valor es un numeo nulo, vamos a llamar a una excepcion.
"""


def mi_funcion(algo=None):
    if algo is None:
        print("Errror! No se permite un valor nulo")

mi_funcion("algo")
mi_funcion()
