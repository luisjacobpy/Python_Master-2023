# Creamos un conjunto vacio
c = set()
print(c)
c.add(1)
c.add(2)
c.add(3)

print(c) # {1, 2, 3}

# Descartar valores
c1 = c.discard(1)
print(c1)
print(c)
c.add(1)
print(c)
c.add(4)

"""
Las colecciones estan referenciadas
"""
# Creamos una copia de 'c' para que los cambios que se realicen no lo afecten
c2 = c.copy()
print(c2)
c2.discard(4)
print(c2) # C2 ya o tiene el 4 pero c tadavia

