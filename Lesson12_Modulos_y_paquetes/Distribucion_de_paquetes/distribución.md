# Distribusión de paquetes
Para crear un paquete distribuible tenemos que crear un fichero especial fuera de la raíz del directorio dentro de nuestro paquete.

## Crear un archivo
Llamado **setup.py** dentro del archivo se va a crear una configuración para la biblioteca `setup tools`.
Este fichero va a contener la configariación del distribuible.

---
## Llamar al arcivo (Step 1)

Desde la terminal ubicandonos en el directorio en donde este el archivo colocamos 
```Bash
python3 setup.py sdist
```
* Se crea el directorio *dist*
* Ingresamos al directorio

 ```Bash
cd dist
```
Corremos **pip install** 

## pip install (Step 2)
```Bash
// Ingresamos
pip install Mensajes-1.0.tar.gz

// Nos arroja
Defaulting to user installation because normal site-packages is not writeable
Processing ./Mensajes-1.0.tar.gz
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: Mensajes
  Building wheel for Mensajes (setup.py) ... done
  Created wheel for Mensajes: filename=Mensajes-1.0-py3-none-any.whl size=2778 sha256=4492d9a750d7a6f63e7b39e4f2119b843a560826b2d2506420b8146ea6d8eb53
  Stored in directory: /home/luisjacobpy/.cache/pip/wheels/b0/f3/35/03a2048feed8e2403e0f2a1ea2c919b49a810ad064bad1c6b4
Successfully built Mensajes
Installing collected packages: Mensajes
Successfully installed Mensajes-1.0
```

## Revisamos que nuestro paquete este distribuido dentro del sistema

```bash
pip list
```
Debe de aparecer nuestro paquete.

---


## Correr nuestro paquete en nuestra maquina local
Abrimos otra terminal, en la raiz de nuestro directorio vamos a correr python
```
python3

// Ingresamos
from mensajes.hola.saludos import saludar

// Nos arroja
Cargando el paquete mensajes...
Cargando el subpaquete mensajes.hola...

// Salimos
exit()
```
---

# Actualizar un paquete
## Agregar el cambio en el paquete
Dentro del subpaquete hola, en el archivo de 'saludos.py' agregamos una nueva función
```python
# Función saludar
def saludar():
    print("Hola te saludo desde saludos.saludar()")
    
def prueba():
    print("Esto es una prueba de la nueva versión")`# Esta es la nueva función
class Saludo():
    def __init__(self):
        print("Hola, te saludo desde Saludos.__init__ ")
```

## Actualizar el archivo setup.py

Dentro del archivo actualizamos la versión
```python
# Importar Modulos
from setuptools import setup

"""Function setup
    params
"""
setup(

    name='Mensajes', #Nombre del paquete
    version='2.0', # version actualizada
    description='Un paquete para saludar y dsepedir',
    author='Luis Jacobo Hernandez',
    author_email='caphumleon@gmail.com',
    url='https://github.com/luisjacobpy',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'], # Incluimos los paquetes y los subpaquetes que hemos creado
    scripts=['test.py'] # Contiene una lista con diferentes scripts que podemos incluir dentro del paquete distribuible.
    
)

```

## Repetimos el paso 1 y 2 con los respectivos nombres
```bash
// Creara la nueva versión
python3 setup.py sdist

// Accedemos al directorio para actualizarla
cd dist

// Desinstala la versión anterior e instala la nueva
pip intall Mensajes-2.0.tar.gz --upgrade

```

## Para borrar un paquete
```
pip unistall nombrepaquete
```