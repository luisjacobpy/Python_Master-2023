"""
Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (Es suficiente con mu=ostrar TRUE or FALSE)
- Si dos numeros son iguales
- Si dos numeros son diferentes
- Si el primero es mayor que el segundo
- Si el segundo es mayor o igula que el primero
"""
# Nombro las variables
primero = int(input('Asiga el valor del primer número: '))
segundo = int(input('Asiga el valor del segundo número: '))

# 1
print(primero == segundo)
# 2
print(primero != segundo)

#3
print(primero > segundo)

#4
print(segundo >= primero)
