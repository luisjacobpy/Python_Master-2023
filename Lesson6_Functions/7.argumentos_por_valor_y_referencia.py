"""
Cuando enviamos información a una funcion generalmente lo hacemos por valor, 
significa que se crea una copia dentro de la funcion de los valores que enviamos
en sus propias variables

[Las colecciones] listas, diccionarios, conjuntos se envian por referencia.
"""
# Ejemplo de paso por valor
def doblar_valor(numero):
    numero*=2 # Multiplicamos por dos

n=10

# Llamamos a la función

print(doblar_valor(2))
print(n)

# Lista de doblare valores
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
# Definimos la lista
ns = [10,50,100]

# Llamamos a la fuinción
doblar_valores(ns) # pasamos como argumento la lista
print(ns) # Output: [20, 100, 200]


"""
Devolver el valor modificado dentro de la función y volver a asignarlo a la variable

"""
def doblar_valor(numero):
    return numero*2 # Multiplicamos por dos

n=10
n = doblar_valor(n)
print(n)

"""
En una colección podemos evitar la modificación creando una copia a la llamada

"""
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
# Definimos la lista
ns = [10,50,100]
doblar_valores(ns[:]) # el slicing indica que quermos devolver una subnlista '(ns[:])'
print(ns) # Output: [20, 100, 200]
