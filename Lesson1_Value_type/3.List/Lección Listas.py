"""
Las listas son elementos mutables, es decir pueden cambiar los elementos que contienen.
"""
# Listas
numeros = [1,2,3,4,5]

datos = [4,"Una cadena",-15,"este es un texto",3.14]

# Para acceder al primer elelemnto de lista
print(datos[0]) #'Nos muestra: 4'

# Podemos hacer Slicing
print(datos[-2:])

#Concatenar con otras listas
print("Esta es una lista con concatenación")
print(numeros + [6,7,8,9])

# Mostrando la mutabilidad
pares = [0,2,4,5,8,10]
print(pares)
pares[3] = 6 # Cambio el indice '5' y lo cambio por el '6'
print(pares)

# Metodo append - Para agregar elementos 
pares.append(12)
print(pares)
pares.append(7*2) # Agregaria 14
print(pares)

# Asignacion con Slicing
letras = ['a','b','c','d','e','f']

# Reasignando valores
letras[:3] = ['A','B','C']
print(letras)

# Eliminar valores con Slicing / Vaciando valores
letras[:3] = []
print(letras)

# Funcion len
print(len(letras))

# Listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c] # Se anidan las listas
print(r)
# para acceder
print(r[0])
# Acceder al primer elemento de la lista a dentro de la lista 'r'
print(r[0][0]) # Estoy apuntando al elemento de la lista a

# Acceder al ultimo elemento de la ultima lista
print(r[-1][-1])
