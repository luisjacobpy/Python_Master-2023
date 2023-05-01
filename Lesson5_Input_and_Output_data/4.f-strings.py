# En lugar de:
nombre = "Hector"
cadena = "Hola {}".format(nombre)
print(cadena)

# Usamos f-string
cadena_2 = f"Hola {nombre}"

print(cadena_2)

# Contenido interpretado
a, b = 10, 5
print(f"La suma de {a} y {b} es {a + b}")

# Con una función
def func():
    return "Pepe"
print(f"Hello {func()}!") # Hello Pepe!

# Diccionario
number = {"uno":1, "dos":2, "tres":3}
print((f"El número dos es: {number['dos']}")) # El número dos es: 2

# ALineacion
print(f"{'Hola Mundo':40}") # Alineación a la izquierda con 40 caracteres

# Truncamiento
print(f"{'Hola Mundo':.4}")  # Hola

# Trucamiento con variables
limite = 4
print(f"{'Hola Mundo':.{limite}}") # Hola

# Formateo de numeros enteros rellenados con espacios / 
print(f"{1:6d}")
print(f"{10:6d}")
print(f"{100:6d}")
print(f"{1000:6d}")
print(f"{10000:6d}")
print(f"{100000:6d}")
# Output
"""
     1
    10
   100
  1000
 10000
100000
"""

# Formateo de numeros float rellenados con espacios / 
# 4 digitos: 3 enteros, 1 punto y 3 decimales
print("\nSe imprime: Formateo de numeros float rellenados con espacios ")
print(f"{3.1415926:9.4f}")

# Formateo de numeros float rellenados con ceros / 
# 4 digitos: 3 enteros, 1 punto y 3 decimales
print("\nSe imprime: Formateo de numeros float rellenados con ceros ")
print(f"{3.1415926:09.4f}")