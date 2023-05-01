class Producto:
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

al = Alimento(2035,"Botella de aceite de Oliva Extra",5,"250 ML")
# Asignamos el resto de valores por fuera
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"


libro_1 = Libro(2023,"Cocina Mexicana", 345,"Cocina tradicional Oaxaca")
libro_1.isbn = "cod-000123"
libro_1.autor = "Fondo de cultura economica"

# Añadimos los productos a una lista
productos = [ad, al] # Adorno y alimento
productos.append(libro_1)


"""
Al modificar el valor por referencia, estamos modificando el valor del objeto/variable original.
Si queremos hacer una copia usamos `copy`
"""
import copy
copia_ad = copy.copy(ad)
print(copia_ad) #25

# Agrego al pvp 25
copia_ad.pvp = 25
print(copia_ad) #15

# Revisamos el valor del original
print(ad)