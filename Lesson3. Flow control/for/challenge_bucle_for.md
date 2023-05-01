## Bucle for

En este ejercicio se te facilitará un numero aleatorio que no conoces en la variable numero.

Utilizando lo que conoces sobre los bucles for y la función range() , debes realizar un sumatorio de todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples de 5 y 7, y almacenarlo en la variable sumatorio.

Ejemplo, si numero fuera 7, el sumatorio sería igual a 1+2+3+4+6 = 16.

Recuerda, únicamente debes sumar los números NO múltiples de 5 y 7 al sumatorio.

### My solution
```python
from evaluate import numero

sumatorio = 0

# Completa el ejercicio aquí

for number in range(0,numero+1):
    if number % 5 != 0 and number % 7 != 0:
        sumatorio += number
    
```
### Teaher's solution
```python
from evaluate import numero
 
# Completa el ejercicio aquí
sumatorio = 0
 
# Generamos el bucle entre 0 y el numero+1 (para no excluirlo del range)
for n in range(numero+1):
    # Si no es múltiple de 5 y 7 lo sumamos
    if n % 5 != 0 and n % 7 != 0:
        sumatorio += n
```
