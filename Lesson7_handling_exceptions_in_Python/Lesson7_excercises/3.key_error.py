"""
Key error

"""

colores = {'rojo':'red', 'verde':'green', 'negro':'black'}

try: 
    colores['blanco']
except KeyError:
    print("Error: la clave del siccionario no se encuentra, debes probar con otra que si exista.")