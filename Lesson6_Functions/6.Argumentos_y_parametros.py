def resta(a,b): # Parametros
    return a-b

r = resta(1,2) #Argumentos


print(r)

resta(b=2,a=1) # Hacemos referencia direecta a los parametros

"""
Asignar valores por defecto
"""
def resta_2(a=None, b=None): # Definimos con valores nulos
    if a == None or b == None:
        print("Ingresa un valor a la función")
        return
    
    return a-b
print(resta_2(2,3))