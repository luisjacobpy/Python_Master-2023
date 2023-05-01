"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
Al parecer contiene el nombre de un alumno y la tota del examen.
Debemos formatear la cadena y conseguir un aestructura:
Nombre Apellido ha sacado una nota

** Recordar para voltear una cadena de texto utilizando slicing:
 cadena[::-1]
"""
cadena = "zeréP nauJ,01"

# Desarrollo de solución
cadena = cadena[::-1]
nombre = cadena[3:]
nota = int(cadena[:2])
# Output
print(f"{nombre} ha sacado un {nota} de nota")
