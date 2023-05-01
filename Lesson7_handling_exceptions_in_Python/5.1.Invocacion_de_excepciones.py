"""
El código es una función en Python llamada mi_funcion que tiene un parámetro opcional algo que está inicializado en None por defecto.
La función verifica si el valor de algo es nulo utilizando una declaración if y en caso de que sea nulo, 
se lanza una excepción ValueError con el mensaje de error "Error! No se permite un valor nulo" utilizando la declaración raise.

La función también utiliza un bloque try-except para manejar la excepción ValueError que se ha lanzado.
Si se produce la excepción, se imprimirá un mensaje de error "Error! No se permite un valor nulo (desde la excepción)" utilizando la declaración print.
Por último, la función se llama sin ningún argumento (mi_funcion()) lo que debería provocar que se lance la excepción y se imprima el mensaje de error 
"Error! No se permite un valor nulo (desde la excepción)".

"""


def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError ("Error! No se permite un valor nulo") # Raise sirve para invocar
    except ValueError:
        print("Error! No se permite un valor nulo(desde la excepción)")

mi_funcion() # Errror! No se permite un valor nulo