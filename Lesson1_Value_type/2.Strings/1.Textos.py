""""
Lección 2. Textos

""""
# Caracter de escape
# Ejemplo 1
"Esta \"palabra\" se encuentra entre conillas dobles"
# Ejemplo 2
"Esta \'palabra\' se encuentra entre conillas dobles"

print("Esta \'palabra\' se encuentra entre conillas dobles")

# Cadena de caracteres con una tabulación
print("Un texto\tuna tabulación")
# Una nueva linea / Salto de linea
print("Un texto\nuna nueva linea")

# Evitar que nos interprete los caracteres especiales
print(r"C:\nmombre\directorio") # Le indicamos que es una cadena de tipo crudo

# Mostrar una cadena escrita en varias lineas
print(""" 
      Una linea
      Otra linea
      Ultima linea
      """)
# Guargar una cadena dentro de una variable
c = "Esto es una cadena"
print(c)

# Suma de cadenas / Concatenación
print(c+c)
