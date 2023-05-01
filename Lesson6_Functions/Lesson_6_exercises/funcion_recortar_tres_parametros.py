"""
Realiza una función llamada recortar que reciba tres parametros. 
El primero es el numero a recortar 
El segundo es el limite infeior
El tercero es el limite superior

La función tendrá que cumplir lo  siguiente:
> Devolver el limite inferior si el numero es menor que este
> Devolver el limite siperior si el numero es mayor que este
> Devolver el numero sin cambios si no se supera ningun limite

a = numero a recortar
b = limite inferior
c = limite superior
"""
def recortar(a,b,c):
    if a < b:
        return b
    elif a > c:
        return c
    elif a >= b and a <= c:
        return a
print(recortar(15,0,10))
print(recortar(1,0,10))
print(recortar(-2,0,10))

"""
Testing process: OK

"""
