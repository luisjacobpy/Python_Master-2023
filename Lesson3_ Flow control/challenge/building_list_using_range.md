Utilizando l afunción range() y la conversion a listas genera las siguientes listas dinamicamente:

Todos los números del 0 al 10
Todos los números del -10 al 0
Todos los números pares del 0 al 20
Todos los números impares del -20 al 0
Todos los números multiplos de 5, del 0 al 50

```python
list_1 = (list(range(0, 11)))
print(list(range(0, 11))) # 0 al 10
print(list(range(-10, 1))) # -10 al 0
print(list(range(0, 21, 2))) # 0 al 20
print(list(range(-19, 1, 2))) # -20 al 0 / impares
print(list(range(0, 51, 5)))# 0 al 50
```
### Output
```Bash
list_1 = (list(range(0, 11)))
print(list(range(0, 11))) # 0 al 10
print(list(range(-10, 1))) # -10 al 0
print(list(range(0, 21, 2))) # 0 al 20
print(list(range(-19, 1, 2))) # -20 al 0 / impares
print(list(range(0, 51, 5)))# 0 al 50
```
