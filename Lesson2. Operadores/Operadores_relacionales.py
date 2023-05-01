"""
Se agrega el print par apoder vcer el valor devuelto en la consola
"""
# Igual que

print(3 == 2)

# Distinto de
print( 3 != 2 )

# Mayor que
print( 3 > 2 )

# Menor que
print( 3 < 2 )

# Mayor o igual que
print(3 >= 2)

# Menor o igual que
print(3 <= 2)
# Tambien podemos utilizar variables
a = 10
b = 5

print( a != b)

print( a == b*2 )

# Comparando cadenas
print("Hola" == "Hola")

c = "Hola"
print(c[0] == "H")
print(c[-1] == "a")

# Listas
l1 = [0,1,2]
l2 = [2,3,4]

print(l1 == l2)
# La longitud de l1 es igual a la longitud de l2
print(len(l1) == len(l2))
# El ultimo elemento de l1 es igual al ultimo elelemnto de l2
print(l1[-1] == l2[0])
"""
True quivale a un 1
False equivale a 0
"""
print(False != True)
