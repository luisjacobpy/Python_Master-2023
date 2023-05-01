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
Productor 
Distribuidor

Los libros:
ISBN
Autor

"""
class Producto:
    """Super clase producto
    
    Subclases:
    Adorno
    Alimiento
    Libro
    """
    def __init__(self,referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp # Precio de venta al publico
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
        
# Creacion del objeto
adorno = Producto('000A','ADORNO','Vaso adornado',15,'Vaso de porcelana con dibujos')

print(adorno) # ADORNO

        
        