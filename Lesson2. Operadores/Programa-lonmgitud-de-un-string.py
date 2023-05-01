"""
Utilizando operadores logicos, dertermina si una cadena de texto introducida por el usuario
tiene una longitud mayor o igual que 3 y a su vez es menor que 10.
"""
cadena = str(input("Introduce una cadena de Texto: "))
print('Cadena ingresada:', cadena)
leng_cadena = len(cadena)
print('La longitud de la cadena es:', leng_cadena)
print('la longitud de la cadena es mayor o igual que 3, y menor que 10:', (len(cadena) >=3) and (len(cadena) < 10))
