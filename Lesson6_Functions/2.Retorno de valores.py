
"""
Imaginemos que queremos retornar una cadena de texto

"""
def test():
    return "Una cadena retornada"

test() # Llamada a la función

print(test())

# Para guardar el valor retornado
c = test()

"""
Ejemplo con copleccion de datos
"""
def test_2():
    return [1,2,3,4]
print(test_2())

print(test_2()[-1]) # Para ver el ultimo elemento

"""
Devolver multiples valores separados por comas
"""
def test_3():
    return "a sreing",20,[1,2,3]
print(test_3()) # Retorna un Class Tuple

# Asignar los valores 
c,n,l = test_3()