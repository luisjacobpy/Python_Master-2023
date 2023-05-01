"""
Herencia en un sistema de adminsitración de una tienda

Prodcutos:
Adornos
Alimientos
Libros

Todos los productos tienen:
Referencia
Nombre
Precio
Descripción

Los alimentos tenian:
    -Productor 
    -Distribuidor

Los libros:
    -ISBN
    -Autor

"""
class Producto:
    """Super clase producto
    Subclases:
    - Adorno
    - Alimiento
    - Libro
    """
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp # Precio de venta al publico
        self.descripcion = descripcion
        
    # Add metodo string que devuelva un string que explique el producto
    def __str__(self):         
        return f"""\
    REFERENCIA\t{self.referencia}
    NOMBRE\t{self.nombre}
    PVP\t{self.pvp}
    DESCRIPCIÓN\t{self.descripcion}
    """

class Adorno(Producto):
    pass

class Alimento(Producto):
    """Clase alimento que hereda de producto
    """
    productor = ""
    distribuidor = ""
    
    def __str__(self): # Sobre escriibimos el string
        return f"""\
    REFERENCIA\t{self.referencia}
    NOMBRE\t{self.nombre}
    PVP\t{self.pvp}
    DESCRIPCIÓN\t{self.descripcion}
    PRODUCTOR\t{self.productor}
    DISTRIBUIDOR\t{self.distribuidor}
    """
    
class Libro(Producto):
    """Clase Libro que hereda de producto
    """
    isbn = ""
    autor = ""
    
    def __str__(self): # Sobre escriibimos el string
        return f"""\
REFERENCIA\t{self.referencia}
NOMBRE\t\t{self.nombre}
PVP\t\t{self.pvp}
DESCRIPCIÓN\t{self.descripcion}
ISBN\t\t{self.isbn}
AUTOR\t\t{self.autor}
"""
# Creacion del objeto
ad = Adorno('000A','Vaso adornado',15,'Vaso de porcelana con dibujos de arboles')
print(ad) # ADORNO

al = Alimento(2035,"Botella de aceite de Oliva Extra",5,"250 ML")
# Asignamos el resto de valores por fuera
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"
print(al)
libro_1 = Libro(2023,"Cocina Mexicana", 345,"Cocina tradicional Oaxaca")
libro_1.isbn = "cod-000123"
libro_1.autor = "Fondo de cultura economica"
print(f"""
DATOS DEL LIBRO:\t
{libro_1}""")


# Añadimos los productos a una lista

productos = [ad, al] # Adorno y alimento
productos.append(libro_1)
print(productos)

# Realizamos un ciclo for par mostrar los productos
print("COLECCIONES\n")
for p in productos:
    print(p,"\n") # Imprimir con salto


print("Atributos\n\n")
for p in productos: # Ciclo for para acceder a atributos
    print(p.referencia,p.nombre,"\n") # Imprimir con salto
    
"""NOTA IMPORTANTE 
Solo se puede acceder a elementos de la clase, no de las sub clases
"""