def saludar():
    print("Hello form the function saludar()")

saludar()

# Podemos crear variables y sentencias
def draw_table_5(): # Función para dibujar la tabla del 5
    for i in range(10):
        print(f"5 * {i} = {i*5}")
        
draw_table_5()
"""
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
"""

# El ambito de las variables de las funciones abarca solo el ambito de su función
m = 300 # Devlaro la variable fuera de la función
def test():
    n = 10
    print(n)
    print(m)
test()

"""
Cuando la variable se encuentra decalrada fuera de la fucnión 
tambien abarca la función.
Podemos definir una variable, unicamente requerimos asignarle valores
antes de llamar a la funión.
Al crear una variable dentro de una función y al reasignarle un valor fuera de la misma, las variables son diferentes auque se llamen igual.

"""
def test_2():
    o = 5
    print(f"Valor dentro de la función:{o}")
test_2()

o = 10
test_2()
print(f"Valor fuera de la función:{o}")
    # Output
"""
Valor dentro de la función:5
Valor dentro de la función:5
Valor fuera de la función:10
"""