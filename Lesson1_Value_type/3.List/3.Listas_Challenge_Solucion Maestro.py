lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# Añadimos los elementos a la primera lista
lista1.append(1234)
lista1.append("Hola")

# Añadimos los elementos a la segunda lista
lista2.append("Adiós")
lista2.append(1234)

# Generamos la tercera lista con los elementos de la primera excepto el último
lista3 = lista1[:-1]

# Generamos la cuarta lista con los elementos de la segunda excepto el primero y el último
lista4 = lista2[1:-1]

# Generamos la quinta lista sumando la cuarta y la tercera
lista5 = lista4 + lista3
