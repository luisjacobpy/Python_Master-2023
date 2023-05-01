
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Método heredado desde la class A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Método heredado desde la class B")

# Subclase

class C(A,B):
    def c(self):
        print("Método heredado desde la subclass C")
c = C() # Hereda de clase A
print(c)

"""
Al crear el objeto se muestra el atributo de la clase A.
Aqui se muestra la prioridad al heredar (desde izquierda)
"""
# Aqui se muestra que el objeto c, Hereda de Class A, Class B Y Subclass C 
print(c.a())
print(c.b())
print(c.c())