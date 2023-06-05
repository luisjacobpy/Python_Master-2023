# Programa

```python
"""
Realiza un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, dewbe repetirse el proceso.
"""

result = False
# Definimos la opción / variable que va a introducir el usario

while result == False:
    user_number = int(input("Introduce un numero par por favor: "))

# Evaluación de la respuesta


    if user_number % 2 == 0:
        print(f"Gracias {user_number}, es un número par")
        result = True
    else:
        print(f"{user_number}, NO es un número par vuelve a intentar")
        result = False
```

## Other solution
