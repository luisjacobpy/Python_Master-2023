## list and for

````python
list = ["Hello!", 10, "Bye!", [50, 100, 150]]

print(list[-1])

## Access
print(list[-1][-1]) # 150

# For in sublist

for number in list[-1]:
    print(number)
# Output
""""
[50, 100, 150]
150
50
100
150
"""
````
## for anidado
````python
"""
Recorrer subelementos dentro de una lista
"""
# list
lista = [
   "This is a string",          # String
    (1,5,10,15,20,25),          # Tuple
    ["Blue","Green", "Yellow"]  # List
]

for collection in lista:
    print(collection)

"""
for anidado
"""
for collection in lista:
    for element in collection:
        print(collection, "->",element)

# Output
"""
This is a string -> T
This is a string -> h
This is a string -> i
This is a string -> s
This is a string ->  
This is a string -> i
This is a string -> s
This is a string ->  
This is a string -> a
This is a string ->  
This is a string -> s
This is a string -> t
This is a string -> r
This is a string -> i
This is a string -> n
This is a string -> g
(1, 5, 10, 15, 20, 25) -> 1
(1, 5, 10, 15, 20, 25) -> 5
(1, 5, 10, 15, 20, 25) -> 10
(1, 5, 10, 15, 20, 25) -> 15
(1, 5, 10, 15, 20, 25) -> 20
(1, 5, 10, 15, 20, 25) -> 25
['Blue', 'Green', 'Yellow'] -> Blue
['Blue', 'Green', 'Yellow'] -> Green
['Blue', 'Green', 'Yellow'] -> Yellow

"""
````
## Enumerate
````python
"""
Anidar dos enumeraciones
"""
# Variable
lista = [
   "This is a string",          # String
    (1,5,10,15,20,25),          # Tuple
    ["Blue","Green", "Yellow"]  # List
]


# Enumerate
for indice_collection, collection in enumerate(lista):
    for indice_element, element in enumerate(collection):
        print(collection, "->",element)

# Output
"""
This is a string -> T
This is a string -> h
This is a string -> i
This is a string -> s
This is a string ->  
This is a string -> i
This is a string -> s
This is a string ->  
This is a string -> a
This is a string ->  
This is a string -> s
This is a string -> t
This is a string -> r
This is a string -> i
This is a string -> n
This is a string -> g
(1, 5, 10, 15, 20, 25) -> 1
(1, 5, 10, 15, 20, 25) -> 5
(1, 5, 10, 15, 20, 25) -> 10
(1, 5, 10, 15, 20, 25) -> 15
(1, 5, 10, 15, 20, 25) -> 20
(1, 5, 10, 15, 20, 25) -> 25
['Blue', 'Green', 'Yellow'] -> Blue
['Blue', 'Green', 'Yellow'] -> Green
['Blue', 'Green', 'Yellow'] -> Yellow
"""
````

## Enumerate
```python
# Enumerate
for indice_collection, collection in enumerate(lista):
    for indice_element, element in enumerate(collection):
        print(lista[indice_collection][indice_element])

# Variable
table = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

for fila in table:
    for columna in fila:
        print(columna, end=" ")
```
