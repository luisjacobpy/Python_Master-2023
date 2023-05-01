"""

Un metodo es una funcion dentro de una clase
el metodo: __init__(self)
El metodo 'init'es un metodo especial que se ejecuta al crear un objeto.


"""
class Galleta():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta")

g = Galleta()