"""
Funciones integradas
"""
n = int("10") # Para transformar en un entero
f = float("10.5")

# Para transformar una cadena y numero a una cadena utulizo 'str()'
c = "Un texto y un numero " + str(10) + " " + str(3.14)
print(c) # Un texto y un numero 10 3.14
print(type(c)) # Un texto y un numero 10

# Convertir un numero entero a binario
bi = bin(10)
print(bi) # 0b1010

# Convertir un numero entero a Hexadecimal
h = hex(10)
print(h) # 0xa
# Convertir un numero binario a entero
i = int('0b1010',2) #el 2 se coloca para especificar que esta en binario

# Convertir un numero hexadecimal a entero
h = int('0xa', 16)
print(h)

# Valor absoluto
print(abs(10)) #10
print(abs(-10)) #10, porque cuenta la distacia ha hay desde el valor hasta el 0

# Redondeo 'round()'
r= round(5.4)
print(r) # 5
r_1= round(5.6)
print(r_1) # 6

# Evaluar 'eval'
print(eval('2+5')) #7

# Otro ejemplo de 'eval()'
n1 = 10
print(eval("n*10 - 5")) # 95

# 'len()' para saber la longitud de una cadena
print(len("Una cadena")) # 10
print(len([])) # 0

# Acceder a la funcion de ayuda de python
# help() # Accedes a la funcion de ayuda y documentacion

def test(num):
   return num, num*2, num*4
 
print(test(5)) # (5, 10, 20)

