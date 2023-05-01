"""
Indices y slicing
"""

# Para acceder a algun caracter de una cadena necesitamos los indices

# Asignamos el string a la variable
palabra = "Python"
#Indices
print(palabra[1])
# Indices en negativo, se inicia a contar en negativo desde el ultimo caracter de la cadena
print(palabra[-6]) # Nos imprime la 'P'
"""
Slicing
"""
print(palabra[0:2])  #'Imprime Py'\

# Imprimir desde el indice 2 al final
print(palabra[0:])
print(palabra[:2] + palabra[2:]) #'Imprime Python'

# Funcion len / Nos da la longitud
print(len(palabra))
