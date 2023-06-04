# Distribusión de paquetes

Para crear un paquete distribuible tenemos que crear un ficheo especial fuera de la raiz del directorio dentro de nuestro paquete.


## Crear un archivo
Llamado **setup.py** dentro del archivo se va a crear una configuración para la biblioteca setup tools.
Este fichero va a contener la configariación del distribuible.

## Llamar al arcivo

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

## Correr nuestro paquete en nuestra maquina local
Abrimos otra terminal, en la raiz de nuestro directorio vamos a correr python
```
python3

// Ingresamos
from mensajes.hola.saludos import saludar

// Nos arroja
Cargando el paquete mensajes...
Cargando el subpaquete mensajes.hola...
```