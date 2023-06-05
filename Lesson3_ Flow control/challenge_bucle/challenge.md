Bucles anidados
En este ejercicio se te va a facilitar una variable matriz repleta de números enteros y de la cuál lo único que sabes es que contiene dos dimensiones.

Aquí tienes una estructura de ejemplo ilustrando como se forma (lista con sublistas), muy parecida a una tabla:

matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]
El objetivo del ejercicio es modificar su contenido dinámicamente, sustituyendo todos sus números pares por 0 y los impares por 1.

Siguiendo el ejemplo anterior la matriz tal como quedará después de que la modifiques sería así:

matriz = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0]
]
Notas:

Una forma de entender una matriz bidimensional es como una tabla compuesta de filas y columnas.

Las filas y columnas se representan como listas anidadas y eso significa que se pueden recorrer mediante bucles for anidados.

Comúnmente al índice que recorre las filas se le denomina i y al de las columnas j, tal como muestra la imagen inferior.

Para acceder a una posición dinámicamente será necesario entonces utilizar ambos índices, tal que así: matriz[i][j]

Recuerda utilizar la función enumerate para conseguir los índices, teniendo en cuenta que primero se recorren las filas y de ellas las columnas, siendo cada columna el propio valor a tratar.


```python
from evaluate import matriz
 
# Primero recorremos todas las filas de la matriz con un for
# Necesitamos usar un enumerador para poder guardar su índice de fila
for i, fila in enumerate(matriz):
    # Dentro de cada fila recorremos cada columna con otro for
    # Necesitamos usar un enumerador para poder guardar su índice de columna
    for j, columna in enumerate(fila):
        # A partir de ambos índices podemos comprobar la celda actual
        # Si es par asignamos a la celda un 0
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        # En caso contrario, si es impar, le asignamos un 1
        else:
            matriz[i][j] = 1
```
# Other option
```python
matriz = [
    [8, 7, 0],
    [34, 2, -1],
    [5, -5, 12]
]

"""
i = lo usamos para las filas
j = lo usamos para recorrer las columnas
"""
# Primero recorremos todas las filas de la matriz con un for: 'for i'
# Necesitamos usar un enumerador para poder guardar su índice de fila: 'fila in enumerate'
for i, fila in enumerate(matriz):
    # Dentro de cada fila recorremos cada columna con otro for
    # Necesitamos usar un enumerador para poder guardar su índice de columna
    for j, columna in enumerate(fila):
        # A partir de ambos índices podemos comprobar la celda actual
        # Si es par asignamos a la celda un 0
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        # En caso contrario, si es impar, le asignamos un 1
        else:
            matriz[i][j] = 1
```
