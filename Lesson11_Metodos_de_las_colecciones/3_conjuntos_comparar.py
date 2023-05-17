"""
Comparar varios conjuntos
1- Comprobar si un conjunto es disjunto de otro, es decir si no hy ningun elelmento en comun
2- Comprobar si un conjunto es subconjunto de otro, si se encuentra completamente dentro de otro conjunto
3- Comprobar si es un conjunto contenedor de otro subconjunto.

"""
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

"""
Para evaluar si un conujnto es disjunto, es decirt no hay ningun elemento comun entre ellos
"""
# isdisjoint
print(c1.isdisjoint(c3)) # True / No concuerda ningun elemento entre ellos

print(c1.isdisjoint(c2)) # False / Concuerda algun elemento

# Comprobar si es un subconjunto

print(c1.issubset(c4)) # se evalua: c1 es subconjunto de c4 / True

print(c3.issubset(c4)) # False

# Comprobar si es un superconjunto / es un contenedor

print(c4.issuperset(c1)) # True

print(c3.issuperset(c1)) # False
