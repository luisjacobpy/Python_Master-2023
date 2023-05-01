"""
Funcion con parametros indeterminados (*args)
"""
def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5,"Hola",[1,2,3,4,5]) # Output: (5, 'Hola', [1, 2, 3, 4, 5])

"""
 Funcion para recorrer los argumentos 
"""

def indeterminados_posicion(*args):
    for arg in args:
        print(arg) 

indeterminados_posicion(5,"Hola",[1,2,3,4,5]) # Output: (5, 'Hola', [1, 2, 3, 4, 5])

"""
Funcion para crear un diccionario
"""

def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])

"""
    Recorremos con un for, para que nos muestre las claves
"""

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg]) # Imprime la clave del diccionario y el valor
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])
#Output
"""
n   5
c   Hola
l   [1, 2, 3, 4, 5]
"""
"""


"""

def super_function(*args,**kwargs):
    t = 0 # variable del total
    for arg in args:
        t=+arg # Suma en asignacion
    print("Sumatorio de indeterminado es", t) #Nos muestra el total
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])
super_function(10,50,-1,)
    

