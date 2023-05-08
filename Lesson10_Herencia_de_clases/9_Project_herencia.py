"""
Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos
Crea una función llamada 'catalogar()', que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
Modifica la función 'catalogar' para que reciba un argumento optativo 'ruedas'
haciendo que se muestre unicamente los que su número de ruedas concuerde con el valor del argumento


Recordatorio: Puedes utiilizar el atributo especial de la clase name de la siguiente forma para recuperar el nombre de la clase de un objeto.
type(objeto).__name__
"""
# Super Class
class Vehiculo():
    def __init__(self, color, ruedas):
            self.color = color
            self.ruedas = ruedas
            
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)
        
    # Sub class
class Coche(Vehiculo):
            
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) # Utilizamos super() sin self en lugar de vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

            # Completa el ejercicio aqui
            
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada) # Utilizamos super() sin self en lugar de vehiculo
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kilos de carga".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas) # Utilizamos super() sin self 
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


    

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo) # Utilizamos super() sin self 
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)
    

# Creamos listas
vehiculos = [
    Coche("blue", 4, 150, 1200),
    Camioneta("white", 4, 100, 1300, 1500),
    Bicicleta("green", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

# Funciones
def catalogar(lista):
    contador = 0 # Establecemos un contador
    for v in vehiculos: 
        contador += 1 # Incrementamos el contador
    print(f"Se han encontrado {contador} vehiculos:\n")
    print("============================================")
        
    for v in lista:
        print("{} {}".format( type(v).__name__, v))
# Inicializamos la funcion



def catalogar_filter(lista, ruedas=None):
    
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas:")
    for v in lista:
        if ruedas == None:# Vamos  a copmprobar si ruedas es igual a None, significa que no hemos pasado el filtro por lo tanto vamos a mostrar todos los elementos de la lista
            print("{} {}".format( type(v).__name__, v))
        elif v.ruedas == ruedas:
            print("{} {}".format( type(v).__name__, v))
            
# llamada a las funciones
print("Catatogar\n")
catalogar(vehiculos) 
print("============================================")
print("\nCatatogar (Filter)\n")
catalogar_filter(vehiculos, 2) # Llamamos a la funcion dilter y le pasamos el parametro