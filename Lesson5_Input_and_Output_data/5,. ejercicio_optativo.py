"""
Formatea los siguientes valores para mostrar el resultado indicado

"Hola mundo" --> Alineao a la derecha en 20 caracteres
"Hola mundo" --> Truncamiento en el cuassto caracter indice 3
"Hola mundo" --> Alineamiento al centro en 20 caracteres con truncamiento en el segundo caracter(indice 1)
150 --> Formateo a 5 numeros enteros rellenados con numeros
7887 --> Formateo a 7 numeos rellenados con espacios
20.02 --> Formateo a 3 números enteros y 3 decimales

"""

# Resuelve el ejercicio aqui

print("{:>20}".format("Hola mundo")) # Alineao a la derecha en 20 caracteres
print("{:.3}".format("Hola mundo"))# Truncamiento en el cuasto caracter indice 3
print("{:^20.1}".format("Hola mundo")) # Alineamiento al centro en 20 caracteres con truncamiento en el segundo caracter(indice 1)
print("{:05d}".format(150))
print("{:7d}".format(150))
print("{:07.3f}".format(150)) # Formateo a 3 números enteros y 3 decimales
