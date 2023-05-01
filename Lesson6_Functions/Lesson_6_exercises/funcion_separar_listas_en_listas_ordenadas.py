"""
Realiza una funcion separar() que tome una lista de numeros enteros y devuelva dos listas ordenadas.
La primera con los numeros pares y la segunda con los numeros impares:

Para ordenar utilizamos el metodo sort().
"""
# Creacion de lista
numeros = [-12, 84, 13, 20, -33, 101, 9]

"""
Funcion que separa una lista de pares a impares, toma como argumento una lista
"""
def separar(lista): 
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    # Devolver
    return pares, impares 

pares, impares = separar(numeros) # Por orden se asignan pares con 'return'
print(pares) # [-12, 20, 84]
print(impares) # [-33, 9, 13, 101]