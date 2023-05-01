"""
Una lista se manejo por referencia, mientrtas que un numeo se maneja por valor

"""
a = 10
b = a
print(b) # Output: 10
a = 1000
print(b) # Output: 10, nos vuelve amostrar el valor 

lista1 = [1,2,3,4,5,6,7]
lista2 = lista1
print(lista2) # ontput: [1, 2, 3, 4, 5, 6, 7]
lista1[0] = 1000 # Agregamos un valor al inicio de la lista
print(lista2) # ontput: [1000, 2, 3, 4, 5, 6, 7]

"""
El nuevo valor si se ve reflejado en nuestra lista2
"""

"""
Función para comprobar la direccion en la memoria de un objeto
"""
def memoria(obj):
    print(f"{hex(id(obj))}")

memoria(lista1) # Output: 0x1f2736236c0
memoria(lista2) # Output: 0x1af407b36c0 // tiene la misma direcccion que la lista 1
memoria(a) # Output: 0x21a22a5d790
memoria(b) # Output: 0x18650040210 // son diferentes

"""
No es lo mismo asignar un numero, un caracter o un boolean, que asignar una coleccion: lista o diccionario

"""