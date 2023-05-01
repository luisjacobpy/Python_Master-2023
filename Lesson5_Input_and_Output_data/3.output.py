"""
.format()
"""

# Variables
v = "this is a string"
n = 10 
print("One text", v, "and one number", n) 

# Reformatear la cadena
c = "One text {} and one number 1{}".format(v,n) # indicamos el orden de las variables asignadas
print(c)

# Otra forma de reformatear
print("One text {1} and one number {0}".format(v,n))

# También podemos referenciar a cada variable con un texto
print("One text {texto} and one number {numero}".format(texto=v,numero=n))

# Una forma de referenciar mas simple
print("One text {v} and one number {n}".format(v=v,n=n))
