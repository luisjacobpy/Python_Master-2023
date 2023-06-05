

```python
"""
Enumerate
- Multiple asignation

"""
#
elements  = ["Hi!", 4, "Bye!", [1,2,3]]

# Multiple assignment
a, b, c = 10, 50, 100
print(a, b, c)

# Tupla
(a,b,c) = (10,50,100)

# Enumerator function
#cast use function list
print(list(enumerate(elements))) # [(0, 'Hi!'), (1, 4), (2, 'Bye!'), (3, [1, 2, 3])]

for tupla in enumerate(elements):
    print(tupla)
"""
(0, 'Hi!')
(1, 4)
(2, 'Bye!')
(3, [1, 2, 3])
"""

for indice, valor in enumerate(elements):
    print(indice, valor)

```
## Challenge enumerate
 
### Función enumerate
En este ejercicio se te va a facilitar una variable iniciales que contiene una lista con un número indeterminado de cadenas de texto.

Tu objetivo es modificar las cadenas de esa lista por la letra inicial de cada cadena en la lista utilizando, si lo requieres, la función enumerate.

Supongamos que iniciales tiene el siguiente valor ["Hola", "Mundo"], tu objetivo sería transformar esos valores a ["H", "M"].

Notas:

Recuerda que para modificar los valores en una lista necesitas hacerlo mediante el índice de cada elemento:

```python
from evaluate import iniciales
 
# Recorremos mediante un enumerador cada cadena en la lista
for i,cadena in enumerate(iniciales):
    # Modificamos cada cadena por su letra inicial
    iniciales[i] = iniciales[i][0]s):
    
```

## Challenge n2 Enumerate

### Iteraciones y conversiones
Pide al usuario que introduzca un número entero por teclado entre 1 y 9 (ambos incluidos) y guárdalo en la variable numero. Debes asegurarte de que esa variable numero contiene un numero entero del 1 al 9, utiliza un bucle para repetir la lectura hasta que se cumpla esa condición.

Genera una lista llamada multiplos que contenga los múltiplos de numero en el rango de 1 a 100 (ambos incluidos) utilizando la conversión de un range a list con un paso: list(range(Min,Max,Paso)).

IMPORTANTE:
La función range permite especificar un paso/salto en un tercer argumento, es decir, cada cuantos números se genera uno en el rango. Prueba este ejemplo y saca tus conclusiones, te servirá para solucionar el ejercicio:

list(range(0, 30, 5))  # range con salto de 5
No olvides que la función range incluye el mínimo pero excluye el máximo.

Puedes leer este artículo si necesitas repasar cómo calcular los números múltiplos.
### My code solution
```python
multiplos = []
 
# Empezamos leyendo un número entero por teclado
numero = int(input())
 
# Volveremos a leerlo mientras el número no se encuentre entre 1 y 9 (ambos incluidos)
while numero < 1 or numero > 9:
    numero = int(input())
 
# Generamos con range toda la lista de múltiplos entre el numero y 100
multiplos = list(range(numero, 101, numero))
```
