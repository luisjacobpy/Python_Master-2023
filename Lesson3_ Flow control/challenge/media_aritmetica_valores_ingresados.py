"""
Realiza un programa que pida a l usario cuantos numeros quiere introducir.
Luego lee todos los numeros  y realiza una media aritmética
"""
repeticiones = int(input("¿Cuántos números quieres ingresar?: "))
suma = 0
for r in range(repeticiones):
    suma += float(input("Introduce un número: "))
print(f"Se han introducido {repeticiones}, números que en total han sumado {suma} y la media es:", suma/repeticiones)
