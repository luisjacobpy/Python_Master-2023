"""
Super clase Vehiculo con los atributos: 
Color
Ruedas

Subclase Coche, que hereda los aributos de la Super Clase Vehiculo ademas se agregan los atributos
Velocidad (km/h)
Cilindraje (cc)


Para evitar escribir codIgo innecesario, podemos utilizar un truco que consiste en 
llamar el método de la superclase y luego simplemente escribir el codigo de la clase.

Funcion super()

"""

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    # Sobre escribimos string
    def __str__(self):
        return f"color {self.color}, {self.ruedas} ruedas"
    
# SUBCLASE
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) # Utilizamos super () sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
c = Coche("Azul", 4, 150, 1200)
print(c)
    