Realiza un programa que pida ala usuario un número entero del 0 al 9
y que mientras el numero no sea correcto se repita el proceso.
Luego debe comprobarse si el numero se encuentra en la lista de numeros y notificarlo.

```python
numbers = [1, 3, 6, 9]

# Cicle
while True:
    number = int(input("Write a number between 0 and 9: "))
    if number >= 0 and number <=9:
        break # Break whe cicle is True
# Value in list
if number in numbers:
    print(f"The number: {number} is in the list of numbers: {numbers}")
else:
    print(f"The number: {number} is NOT in the list of numbers: {numbers}")
```

### Output
```Bash
Write a number between 0 and 9: 6
The number: 6 is in the list of numbers: [1, 3, 6, 9]
```
