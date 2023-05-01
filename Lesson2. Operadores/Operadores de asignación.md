Una especie de accesos directos de los operadores aritméticos pero que actúan directamente sobre la variable actual modificando su valor.

Es decir no necesitan dos operandos y solamente una variable numérica. Por eso se les llama operadores de asignación

# Tradicional
a = 0

# Valor de suma en asignación
a+= 1  # Operador de suma en asignación debemos haber delcarado previamente la variabble.
# Con el anteior codigo incrementanmoa el valor en +1 de 'a'
print(a)
a+= 5
print(a)


# Valor de resta en asignación
a -= 10 # Resta en asignación
print(a)

# Producto en asignación
a = 5
a *= 2 # producto de asignación
print(a)


# Division en asignacion
a/= 2 # división en asignación
print(a)

# Modulo en asignacipon
a %= 2 # para saber si es par
print(a)

# Potencia en asignasción
a = 5
a **= 2
print(a)

"""
Ejemplo
"""
n = 0  # Asignación de 0 en n
while n < 10:    # Expresión relacional
    if (n % 2) == 0:   # Expresion aritmetica y expresion relacional
        print( n, 'es un número par')
    else:
        print(n, 'es número impar')
    n += 1 # Expresion aritmetica n = n + 1 equivalente a operación en asignación n+= 1
