"""
Vamos a trabajar con scrips
Importamos el modulo de sys que nos permite analizar algunas de las variables 
y funcionalidades que se cargan durante la ejecucuion con un scrip
"""
import sys

print(sys.argv) # Nos permite analizar los datos que le menadamos a un script durante la ejecucion a través de la linea de comandos.

"""
Para poder ingresar argumentos primero se debe ejecutar el codigo del archivo .py
En la terminal se da tecla arriba par arepetir el codigo y al final de la ruita se agrega el argumento.
"""
"""
Para poder visualizar los argumentos que hemos ingresado
"""
for argumrento in sys.argv[1:0]: # Para mostrar unicamente los argumentos que mhemos iniciado
    print(argumrento)
