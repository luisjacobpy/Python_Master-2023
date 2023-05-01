"""
Funcion recursiva,
cuenta atras

"""
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num) # Llamada a la función
    else:
        print("Se termino el tiempo")
    print("Fin de la función", num)# Para ver el funcionamiento de la función
    
# Llamamos a la función
cuenta_atras(5)


"""
Función del factorial de un numero

"""
def factorial(num):
    print("Valor inicial ->", num)# Para sanber cada vez que se llama al factorial cual es el valor que se le esta pasando
    if num > 1:
        num = num * factorial(num-1)
    print("Valor final ->", num) # Para ver como ha cambiado el valor de num, despues de hacer el factorial
    return num

# Llamamos a la función y le pasamos los argumentos 
factorial(5)

"""
Output:
Valor inicial -> 5
Valor inicial -> 4
Valor inicial -> 3
Valor inicial -> 2
Valor inicial -> 1
Valor final -> 1
Valor final -> 2
Valor final -> 6
Valor final -> 24
Valor final -> 120
"""