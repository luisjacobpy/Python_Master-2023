# Herencia y polimorfismo en python
La herencia y el polimorfismo son dos conceptos fundamentales de la programación orientada a objetos.

La herencia es un mecanismo que permite a una clase heredar los atributos y métodos de otra clase. La clase que hereda se llama subclase o clase derivada, y la clase de la que hereda se llama superclase o clase base. La subclase puede agregar o modificar atributos y métodos heredados, o incluso puede definir sus propios métodos y atributos.

Por otro lado, el polimorfismo se refiere a la capacidad de objetos de diferentes clases para responder a un mismo mensaje o llamada a un mismo método. Esto permite que diferentes objetos que comparten una interfaz común, puedan ser utilizados de manera intercambiable en un programa. En otras palabras, se puede usar una misma función o método para objetos de diferentes clases.

```python
# Definimos la clase Persona, que tiene un método para saludar
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

# Definimos una subclase de Persona llamada Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y estudio", self.carrera)

# Definimos otra subclase de Persona llamada Profesor
class Profesor(Persona):
    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y enseño", self.asignatura)

# Creamos objetos de cada una de las clases
persona = Persona("Juan")
estudiante = Estudiante("María", "Ingeniería")
profesor = Profesor("Pedro", "Programación")

# Llamamos al método saludar de cada objeto
persona.saludar()   # Imprime "Hola, mi nombre es Juan"
estudiante.saludar()   # Imprime "Hola, soy María y estudio Ingeniería"
profesor.saludar()   # Imprime "Hola, soy Pedro y enseño Programación"

```

---
En este ejemplo, creamos una clase base llamada Persona con un método `saludar()`. Luego, definimos dos subclases llamadas Estudiante y Profesor, que heredan el método `saludar()` de la clase base y lo sobrescriben con sus propias implementaciones. Por último, creamos objetos de cada una de las clases y llamamos al método `saludar()` para demostrar el `polimorfismo`, ya que cada objeto responde al mismo mensaje pero con una implementación diferente.

## Función `super()`


super() es una función incorporada en Python que se utiliza para llamar a un método definido en la clase base (superclase) desde una subclase. Permite que las subclases aprovechen el comportamiento ya definido en la superclase sin tener que reimplementar el mismo código.

La función super() se usa generalmente en el método `__init__()` de la subclase para llamar al constructor de la superclase y asegurar que se inicialicen todas las variables de instancia heredadas de la superclase.

Un ejemplo puede aclarar el uso de `super()`. Supongamos que tenemos una clase base llamada `Persona` y una subclase llamada `Empleado`. La subclase `Empleado` hereda de `Persona` el atributo `nombre` y también tiene un atributo adicional llamado `salario`. El método `__init__()` de la clase Empleado necesita inicializar tanto el atributo nombre como el atributo salario. Podemos hacer esto usando super() de la siguiente manera:

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

```

En este ejemplo, la clase `Empleado` hereda de la clase `Persona`. El método `__init__()` de `Empleado` utiliza `super()` para llamar al constructor de la clase `Persona` y establecer el atributo `nombre`. Luego, se inicializa el atributo `salario` en la subclase `Empleado`.

En resumen, `super()` se utiliza en Python para llamar a un método o atributo definido en la superclase desde una subclase. Esto permite que las subclases aprovechen el comportamiento ya definido en la superclase y evita la necesidad de reimplementar el mismo código.

## Herencia múltiple
Hace referencia de que una sub clase herede de varias super clases a la vez, de manera que se pueden heredar gran variedad de atributos y metodos. 
