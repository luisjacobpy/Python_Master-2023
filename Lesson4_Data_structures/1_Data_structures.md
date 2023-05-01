# Colecciones
* Tuplas
* Conjuntos 
* Diccionarios
* Pilas
* Colas


## Tuplas / Tuple
Son inmutables, se utilizan para asegurarnos de que ciertos datos no se puedan modificar.
* Aceptan indexación y slicing
```python
tuple = (100, "Hi!", [1,2,3])
print(tuple)
```
```python
"""
Tuple object does not support item assignment
"""
tuple = (100, "Hi!", [1,2,3], -50)
print(tuple)

# Check the first element
print(tuple[0]) # 100
# Check the last element
print(tuple[-1])  # -50

# Slicing, check second element to the end
print(tuple[1:]) # ('Hi!', [1, 2, 3], -50)

# Acces to list into tuple
print(tuple[2][0]) # 1

# Function len
print(len(tuple))

# Index for search a element
print(tuple.index(100)) # 0
print(tuple.index("Hi!")) # 1

# Count
print(tuple.count(100)) # 1
print(tuple.count(34)) # 0
```

## Conjuntos
Son colecciones desordenadas de elementos unicos.
Se utilizan para hacer pruebas de pertenencia a grupos y eliminación de elementos duplicados.
Se dice que los conjunto s son desordenados porque a medida que añadimos elementos este orden no se conserva.

```python
# Conjunto vacio
# conjunto = set()

# COn valores
conjunto = {1,2,3}
print(conjunto) # {1, 2, 3}

# Metodo Add
conjunto.add(4)
print(conjunto) # {1, 2, 3, 4}

conjunto.add(0)
print(conjunto) # {0, 1, 2, 3, 4}

conjunto.add('H')
print(conjunto) # {0, 1, 2, 3, 4, 'H'}

conjunto.add('A')
conjunto.add('z')

print(conjunto) # {0, 1, 2, 3, 4, 'H', 'A', 'z'}
```
### Comprobar la pertenencia a grupos con conjuntos
```python
grupo = {'Hector', 'Juan', 'Mario'}

print('Hector' in grupo) # True

print('Maria' in grupo) # False

print('Hector' not in grupo) # False

```
### Conjuntos | Eliminar valores repetidos
```python
# Se eliminan los valores repetidos
test = {'Luis','Luis','Luis','Jacobo','Jacobo'}
print(test) # {'Luis', 'Jacobo'}
```
### Conjuntos | Transformando otras colecciones a conjuntos para eliminar duplicados
```python
# Transformando otras colecciones a conjuntos para eliminar duplicados
list_1 = [1,2,3,3,2,1]
# Si hacemos un 'Cast', transformamos esta list_1 a un conjunto.
c = set(list_1)
print(c) # {1, 2, 3}

# Transformamos el conjunto a una lista
list_2 = list(c)
print(list_2) # [1, 2, 3]

# En una sola linea de codigo podemos hacer el cambio
list_1 = [1,2,3,3,2,1]
print(list_1) # [1, 2, 3, 3, 2, 1]
list_2 = list(set(list_1)) #
print(list_2) # [1, 2, 3]

# Para cadenas de caracteres / Stings
s = 'This is a sttring, in string, for string'
print(set(s)) # {'a', ' ', 'r', 'g', ',', 'n', 'o', 'i', 's', 'T', 'f', 'h', 't'}
```

### Conjuntos |Learning_Challenge_Conjuntos
El siguiente ejercicio te servirá para practicar la manipulación de conjuntos.

Debes realizar las siguientes instrucciones de forma ordenada sobre la variable grupo para que el ejercicio valide correctamente:

Añade los siguientes usuarios: Ana, Ramón, Marta, Eric y David (respeta las tildes)

Elimina (*) los usuarios Mario, Miguel y Ramón.

Optativo: Cuando tu solución valide, dale una vuelta de tuerca. A ver si se te ocurre alguna forma de optimizarlo utilizando listas y bucles.

(*) Para eliminar un registro de un conjunto puedes utilizar su método interno conjunto.remove("registro").

```python
# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# Completa el ejercicio
# Add
grupo.add('Ana')
grupo.add('Ramón')
grupo.add('Marta')
grupo.add('Eric')
grupo.add('David')

# Remove
grupo.remove('Mario')
grupo.remove('Miguel')
grupo.remove('Ramón')
print(grupo) # {'Blanca', 'Andrés', 'David', 'Marta', 'Eric', 'Ana'}
  
```
### Other solution
```python
# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
 
# Completa el ejercicio
for usuario in ["Ana", "Ramón", "Marta", "Eric", "David"]:
    grupo.add(usuario)
 
for usuario in ["Mario", "Miguel", "Ramón"]:
    grupo.remove(usuario)
```
## Diccionarios / dict
Los diccionarios junto a las listas on las colecciones más utilizadas en python.
Se basan en ua estructura mapeada donde cada elemento de la coleccion se encuentra identificado con una clave unica
```python
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
```

### Dict , type string and int / using 'for'

```python
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
```

### dict and list
```python
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

```

## Pilas / staks
* Unicamente permite dos acciones 'push' / apilar y 'pop' desapilar
* 'LIFO' (Ultimo en entrar, primero en salir)
* En python como tal no existen las pilas, pero las podemos simular
````python
pila = [3,4,5]
## Adding
pila.append(6)
pila.append(7)

## Sacar elementos
pila.pop() # Sacamos el ultimo elemento
print(pila)
# Si queremos guardar el elemenoto que sacamos de la fila
n = pila.pop() #Guardamos el elemento
print(n)
````
## Colas / queue
FIFO (First in First Out) / Primer en entrar primero en salir
enqueue / encolar : dequeue / desencolar

### Declarar una cola
````python
# Importamos el modulo de cola
from collections import deque
cola = deque()
print(cola)

cola = deque(['Hector','Juan','Miguel'])
print(cola)
# Agregamos elementos
cola.append('Maria')
cola.append('Fernando')
print(cola)
# Sacar elementos de la cola
# Metodo popleft
person_delete = cola.popleft() # Guardo la persona que quite

print(person_delete)
print(cola)
````
