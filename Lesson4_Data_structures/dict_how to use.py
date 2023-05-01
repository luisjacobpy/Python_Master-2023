# Los diccionarios son colecciones desordenadas.
colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green'}
print(colores)
print(type(colores))

# Acceder a valor
print(colores['azul']) #blue

# Se pueden crear inicies de diccionarios tambien con numeros
numeros = {10: 'diez', 20:'veinte'}
print(numeros) # {10: 'diez', 20: 'veinte'}

# Re asignar valores en un Dict
colores['amarillo'] = 'white'
print(colores) # {'amarillo': 'white', 'azul': 'blue', 'verde': 'green'}

# Delete elements in a dict
del(colores['amarillo'])
print(colores) # {'azul': 'blue', 'verde': 'green'}

# Ejemplo
edades = {"Luis": 30, "Kari":27, "Beo": 6}
print(edades)
# Vamos a modificar un valor vamos a sumar/ adding a 'Beo un año'
edades["Beo"]+=1
print(edades)

# Recorrer los elementos de un 'dict' con un ciclo for
for clave in edades:
    print(edades[clave])
# Obtener la clave y su valor
for clave in edades:
    print(clave,edades[clave])
#La forma recomendada es para obtener el valor de las claves es:
for clave, valor in edades.items(): # Es similar al enumerate de las listas.
    print(clave,valor)

# Una de las funciones más avanzadas de los dict es usarlos con las 'list'
"""
Quiero crear una lista de personajes cada personaje tiene un nombre, clase, y una raza.
"""
personajes = []
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
personajes.append(p)
# Agregamos otro personaje
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)
print(personajes)

# Recorremos
for personaje in personajes:
    print(personaje['Nombre'],personaje['Clase'],personaje['Raza'])
