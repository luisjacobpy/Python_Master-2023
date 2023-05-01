# Importamos el modulo math
import math


class Punto:
    def __init__(self, x=0, y=0): # constructor
        self.x = x
        self.y = y
# Sobre escribimos el metodo string
    def __str__(self):
         return "({}, {})".format(self.x, self.y) # Se cambio la linea de codigo
 
 # Metodo cuadrante
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f"{self} pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"{self} pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"{self} pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(f"{self} pertenece al cuarto cuadrante")
        else:
            print(f"{self} Se encuentra sobre el origen")
            
    def vector(self, p):
        print(f"El vector entre {self} y {p} es ({p.x - self.x}, {p.y - self.y}) ")
    
    # Metodo distancia
    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {d}") 
        
"""Clase rectangulo

Con dos puntos (inicial y final) que formaran la diagonal del rectangulo
Contiene un metodo constructor, di no se enviabn los puntos se crearán dos puntos en el origen por defecto.
Metodo base
Metodo altura
Metodo area
"""
class Rectangulo:
    
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x) # Utilizo 'abs' para obtener el valor absoluto en caso de que el resultado sea negativo. 
        print(f"La base del rectángulo es: {self.base}")
    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print(f"La altura del rectángulo es: {self.altura}")
    
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print(f"El área del rectángulo es: {self.area}")

   

    
        
# Creamos los objetos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0) # El origen
O = D

# Llamamos al metodo cuadrante para los objetos creados.
A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()

# Consulta los vectores // En direccion del AB y BA
A.vector(B) # De inicial el A y despues pasamos un vector hasta B
B.vector(A)

"""Ejemplo de respuesta
El vector entre (2, 3) y (5, 5) es (3, 2)
El vector entre (5, 5) y (2, 3) es (-3, -2)
"""
# Consulta la distancia
A.distancia(B)
B.distancia(A)

# Determina cual de los 3 puntos A, B o C, se encuentra mas lejos del origen, punto (0,0)
A.distancia(O) # La variable 'O' corresponde al Origen.
B.distancia(O)
C.distancia(O)


# Creamos un objeto de la clase Rectangulo
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()