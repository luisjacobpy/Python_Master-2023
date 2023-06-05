# adding all the numbers between 0 and 100
```python
"""
Realiza un programa que sume todos los números enteros pares
Desde el 0 hasta el 100
"""

list(range(0,101, 2)) # Se crea una lista usando 'range', el último valor '2', nos indica un salto.

adding = sum( range(0, 101, 2))
print(adding) # Output: 2550


# Other option, more large
num = 0
suma = 0
while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1

print(suma) # Output: 2550

```
