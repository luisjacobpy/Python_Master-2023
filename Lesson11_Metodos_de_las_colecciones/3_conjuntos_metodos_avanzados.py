"""
Metodos avanzados de conjuntos

"""
# Variables
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print(c1.union(c2))

# Comprobamos igualdad
print(c1.union(c2) == c4) # True

print(c1.union(c2))

print(c1)

print(c2)

# Update / para actualizar el resultado de c1 y c2
print(c1.update(c2))
print(c1)

# Encontrar los elementos diferenctes en dos conjuntos
# Variables
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
# Diferencias entre el conjunto 1 y el conjunto 2
print(c1.difference(c2))

# Para guardar la diferencia
print(c1.difference_update(c2))
print(c1) # {1, 2}

# Para ver los elementos comunes
# Variables
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print(c1.intersection(c2))
c1.intersection_update(c2)
print(c1)

# Diferencias simetrica / Devuelve todos los elementos que no concuerdan
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print("==== Diferencia simetrica =======")
print(c1.symmetric_difference(c2))