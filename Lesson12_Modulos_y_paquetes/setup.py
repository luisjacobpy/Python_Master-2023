"""Contiene la configuración del distribuible

"""
# Importar Modulos
from setuptools import setup

"""Function setup
    params
"""
setup(

    name='Mensajes', #Nombre del paquete
    version='1.0',
    description='Un paquete para saludar y dsepedir',
    author='Luis Jacobo Hernandez',
    author_email='caphumleon@gmail.com',
    url='https://github.com/luisjacobpy',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'], # Incluimos los paquetes y los subpaquetes que hemos creado
    scripts=['test.py'] # Contiene una lista con diferentes scripts que podemos incluir dentro del paquete distribuible.
    
)