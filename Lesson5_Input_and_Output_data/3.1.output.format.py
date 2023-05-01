"""
"""

# Alineamiento a la derecha 30 caracteres
print("{:>30}".format("This is an example"))  # Para centrar un texto en una linea de 30 caracteres

# Alineamiento a la izquierda 30 caracteres
print("{:30}".format("This is an example")) # Se crean espacios

# Alinear al centro en 30 caracteres
print("{:^30}".format("This is an example"))

# Truncate, 3 characters
print("{:.3}".format("This is an example"))

# Aligning the characters and Truncate
print("{:>30.3}".format("This is an example"))

"""
    En caso de tener muchas variables hacemos referencia dentro de {} a la variable que mencionamos 
    ejemplo: print("{variable:>30}".format("This is a case"))
"""
"""
format in numbers
"""
# integer formatting, padding with spaces
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

# integer formatting, padding with zeros (0)
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

# formatting of floatings padding with spaces
print("{:.3f}".format(3.1415926)) # 3 float: 3.142

# 
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

# floating formatting, padding with zeros (0)
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))