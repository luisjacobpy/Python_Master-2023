# Español
Este código define dos clases: Punto y Rectangulo. La clase Punto representa un punto en un plano cartesiano, mientras que la clase Rectangulo representa un rectángulo en el mismo plano.

La clase Punto tiene los siguientes métodos:

__init__(self, x=0, y=0): constructor que inicializa las coordenadas x e y del punto. Si no se proporcionan valores, se toman 0 por defecto.
__str__(self): método que devuelve una cadena de texto que representa el punto en formato "(x, y)".
cuadrante(self): método que determina el cuadrante en el que se encuentra el punto. Devuelve un mensaje con el resultado.
vector(self, p): método que calcula el vector entre dos puntos y devuelve un mensaje con el resultado.
distancia(self, p): método que calcula la distancia entre dos puntos y devuelve un mensaje con el resultado.
La clase Rectangulo tiene los siguientes métodos:

__init__(self, pInicial=Punto(), pFinal=Punto()): constructor que inicializa los puntos inicial y final del rectángulo. Si no se proporcionan valores, se crean dos puntos en el origen por defecto.
base(self): método que calcula la base del rectángulo y devuelve un mensaje con el resultado.
altura(self): método que calcula la altura del rectángulo y devuelve un mensaje con el resultado.
area(self): método que calcula el área del rectángulo y devuelve un mensaje con el resultado.
En la parte final del código, se crean varios objetos de la clase Punto y se llaman a varios métodos para realizar diferentes cálculos y obtener resultados en forma de mensajes. También se crea un objeto de la clase Rectangulo y se calcula su base, altura y área.




# Plano cartesiano

Es importante remarcar que el plano se divide en 4 cuadrantes:


## Puntos y coordenadas
El objetivo de esto es describir la posición de puntos sobre el plano en forma de coordenadas, que se forman asociando el valor del **eje de las x (horizontal)** con el valor del **eje Y (vertical).**

## Vectores en el plano
Finalmente, un vector en el plano hace referencia a un segmento orientado, generado a partitr de dos puntos distintos, es decir una linea formada desde un putno inicial en dirección a otro punto final,  por lo que se entiende que un vector tiene longitud y dirección/sentido.


El vector se representaría como la diferencia entre las coordenadas del segundo punto respecto al primero (el segundo menos al primero)

```
AB = (x2-x1, y2-y1) => (5-2, 5-3) => (3,2)
```

# PROGRAMA PLANO CARTESIANO
* Se crea una clase llamada **Punto** con sus dos coordenadas X e Y.
* Se utiliza un método **constructor** para crear puntos fácilmente. Si no reciben una coordenada, su valor será cero.
* Se sobreescribe el método **string**, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
* El método llamado **cuadrante** que indica a qué  cuadrante pertenece el punto, o si es el origen.
* El método **vector**, toma otro punto y calcula el vector resultante entre los dos puntos.
* El método **distancia** toma un c=unto y calcula la distancia entre los dos puntos y lo muestra por pantalla.


