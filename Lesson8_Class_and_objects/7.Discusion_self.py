"""

En python es inportante colocar el self por el Zen de Python, Explicito es mejor que implicito.

"""
class A:
    def __init__(argumento):
        print(argumento)
a = A() # <__main__.A object at 0x000001BD1C43E680>  // Referencia donde se esta almacenando


"""
Creamos una clase Test
"""

class Test:
    contador = 0
    
    def __init__(self):
        Test.contador += 1
        print("Instancias de test creadas ==>", Test.contador)

# Con un bucle for creamos 10 intancias de Test        
for i in range(10):
    Test() 
"""
# Output
Instancias de test creadas ==> 1
Instancias de test creadas ==> 2
Instancias de test creadas ==> 3
Instancias de test creadas ==> 4
Instancias de test creadas ==> 5
Instancias de test creadas ==> 6
Instancias de test creadas ==> 7
Instancias de test creadas ==> 8
Instancias de test creadas ==> 9
Instancias de test creadas ==> 10
"""

# Para revisar cuantas instancias se han creado
print(Test.contador) # 10