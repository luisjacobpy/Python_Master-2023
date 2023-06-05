# Bucle While
* iterar es realizar una acción varias veces
* Cada vez que se repite la acción se llama iteración

### while and else
```python
c = 0
while c <= 5:
    c+=1 # Add +1
    print("c vale:",c)
else:
    print("Finish the iteration")
```
### Breake
````python
c = 0
while c <= 5:
    c+=1 # Add +1
    if (c==4):
        print("We break the bucle when c value:",c)
        break
    print("c vale:",c)
else:
    print("Finish the iteration")
````

### Continue
````python
c = 0
while c <= 5:
    c+=1 # Add +1
    if (c==4):
        print("We are continue whit the next iteration:",c)
        continue
    print("c vale:",c)
else:
    print("Finish the iteration")
````

### Other example
````python
c = 0
while c <= 5:
    c+=1 # Add +1
    if (c==4):
        print("We are continue whit the next iteration:",c)
        continue
    print("c vale:",c)
else:
    print("Finish the iteration and the last value of c is:", c)
````
