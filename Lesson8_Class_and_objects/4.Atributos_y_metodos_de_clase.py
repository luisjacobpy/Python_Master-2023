class Galleta:
    chocolate = False

una_galleta = Galleta()

# Atibutos
una_galleta.sabor = "salado"
una_galleta.color = "marron"

# Mostrar atributos
print(f"El sabor de esta galleta es {una_galleta.sabor}") # El sabor de esta galleta es salado

# Vamos a comprobar si una galleta tiene chicolate
g = Galleta()
print(g.chocolate) # False