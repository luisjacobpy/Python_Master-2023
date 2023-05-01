"""
Realiza una funci'on llamada agregar_una_vez() que reciba una lista y un elemento.
La funcion debe aadir el elemento al final de la lista con la condicion de no repetir ning'un elemento.
Si el elemento ya se encuentra en la lsita se debe invocau un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
    Error: Imposible aadir dlementos duplicados => [elemento].
"""

lista_1 = [1, 5, -2]

def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else: 
            lista.append(el)
    except ValueError:
        print(f"Error: Imposible aadir dlementos duplicados => {el}.")

agregar_una_vez(lista_1,2)
agregar_una_vez(lista_1,5) # Imposible aadir dlementos duplicados => 5.
    