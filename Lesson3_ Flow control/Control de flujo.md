# Control del flujo
* Se entiende así a la secesión de instrucciones de un programa informatico.
* Se ejecutan unas tras otras de manera ordenana.
* Tienen el objetivo de manipular información.

## Condicionales
Para elegir entre distintas posibilidades.


## Interativas
Para repetir un bloque de instrucciones.


## Sentecia IF 
permite dividir el flujo de un programa en diferentes caminos

```python
'''
Ejemplo 1
'''
a = 5
b = 10
if a == 5:
    print("a vale:", a)
    if b == 10:
        print("y b vale:", b)
'''
Ejemplo 2
'''
c = 5
d = 10
if c == 5 and d = 10:
    print("c vale 5 y d vale 10")
```
## Sentencia ** else **
Se enadena a un if para indicar el caso contrario cuando no se cumple la condión.

```python
'''
Else / Elif
Determinar si es un numero par o impar
'''

n = 10
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")


```

## Sentencia elif
```python
'''
Creando un comando con elif
'''
print("Ejemplo de un comando con elif")
comando = "Salir"
if comando == "Entrar":
    print("Bienvenido al sistema")
elif comando == "Saludar":
    print("Hola, espero que te lo estés pasando bien aoprndiendo python")
elif comando == "Salir":
    print("Saliendo del sistema")
else:
    print("Comando no reconocido")

'''
Creando un programa para revisar notas
'''
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("notable")
elif nota >=6:
    print("Bien")
elif nota >=5:
    print("Suficiente")
else:
    print("Insuficiente")


```


## Sentencia Match-Case (Python 3.10)
En Python 3.10 se ha añadido una nueva sentencia condicional inspirada en el clásico switch-case de los lenguajes basados en C, se trata de match-case.

Esta sentencia permite evaluar un valor y definir diferentes casos para actuar en consecuencia, de manera que en lugar de un if con múltiples elif como el siguiente:
````python
opcion = input()
 
if opcion == "A":
    print("Opción A")
elif opcion == "B":
    print("Opción B")
elif opcion == "C":
    print("Opción C")
else:
    print("Opcion por defecto")
````
### Se puede realizar lo siguiente:
````python
opcion = input()
 
match opcion:
    case "A":
        print("Opción A")
    case "B":
        print("Opción B")
    case "C":
        print("Opción C")
    case _:
        print("Opción por defecto")
````
Lo único destacable es el caso por defecto que se específica con _, por lo demás es prácticamente lo mismo y considerando que no todos estamos utilizando Python 3.10 creo que aún no vale la pena profundizar demasiado.
