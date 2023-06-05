## My solution
A partir de dos variables nombre  y edad crea una variable expresion que almacene si se cumplen TODAS las siguientes condiciones encadenando operadores lógicos en una sola línea:

Que nombre sea diferente de cuatro asteriscos.

Que edad sea mayor que 10 y a su vez menor que 18.

Que la longitud del nombre sea mayor o igual que 3 pero a la vez menor que 10.

Nota: Utiliza paréntesis para encadenar diferentes conjuntos de expresiones lógicas entre ellas.

Por cierto, en este ejercicio edad y nombre se cargarán durante la solución así que no sabes qué contienen, no les des ningún valor manualmente o el test fallará.

```py
# no borres esta línea
from evaluate import edad, nombre

# completa el ejercicio
expresion = (nombre != "****") and (edad > 10 and edad < 18) and (len(nombre) >= 3 and len(nombre) < 10)


# Nombre sea diferente a '****'
# Edad >10 and Edad < 18
# Longitud de nombre nombre(len) sea mayor o igual que 3 pero a la vez menor que 10
```

## Teacher's solution
```py
# no borres esta línea
from evaluate import edad, nombre
 
# completa el ejercicio
expresion = (nombre != "****" and len(nombre) >= 3 and len(nombre) < 10) and (edad > 10 and edad < 18)
```
