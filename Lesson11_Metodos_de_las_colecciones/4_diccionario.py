colores = {
    "amarillo":"yellow", "azul":"blue", "verde":"green", "rojo":"red", "negro":"black"
           }
# Para conocer el valor
print(colores["amarillo"])

# Conseguir un valor
print(colores.get('amarillo', 'no se encuetra')) # No se encuentra se acciona en caso de que agreguemos un argumento inexistente


# conocer si se encuentra dentro de colores
print('amarillo' in colores) # True
print('negro' in colores) # True
print('blanco' in colores) # False

# Sacar una lista con las claves de un diccionario
print(colores.keys()) # dict_keys(['amarillo', 'azul', 'verde', 'rojo', 'negro'])

# Conocer los valores del diccionario
print(colores.values()) # dict_values(['yellow', 'blue', 'green', 'red', 'black'])

# Para obtener los valores y las claves a la vez
print(colores.items())

# utilizando form
for c in colores:
    print(colores[c])
# Optimizar for
# Mostrar las claves
for c in colores.keys():
    print(c)

# Mostrar los valores
for c in colores.values():
    print(c)
    
# Mostrar ambas cosas
for c,v in colores.items():
    print(c,v)
    
# Sustraer valores
colores.pop("amarillo", "no se ha encontrado")
print(colores)


# Podemos vaciar un diccionario
colores.clear()
print(colores)