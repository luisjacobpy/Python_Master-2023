#append
lista = [1,2,3,4,5]
lista.append(6)
print(lista)

# Clear
lista.clear()
print(lista)

# Unir listas con extend
l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)
print(l1) # [1, 2, 3, 4, 5, 6]

print(["Hola", "mundo", "mundo"].count("mundo")) # 2

# Index para el indice
print(["Hola", "mundo", "mundo"].index("mundo")) # 1

# INSERT Para agregar un elemento dentro de la lista
l = [1,2,3]
l.insert(0,0)

print(l) # [0, 1, 2, 3]

l = [5,10,15,25]
l.insert(-1,20)
print(l)

# POP eleminar elementos de la lista
l = [10,20,30,40,50]
print(l)
v = l.pop()
print(v)
print(l)

# Para eliminar el primer elemnto
v2 = l.pop(0)
print(l)

# Para borrar un valor
l.remove(30) # Solo elimia el primer elemento que coincida
print(l)

# Para darle la vuelta a una lista
l4 = [20, 30, 30, 40]
l4.reverse()
print(l4)

# Para voltear una cadena
lista = list("Hola mundo")
print(lista)

# Uso de reverse
lista.reverse()
print(lista)
# Uso de join
cadena = "".join(lista)
print(cadena)

# Ordenar elementos de una lista
lista = [5, -10, 35, 0, -65, 100]

lista.sort()
print(lista)
lista_mayor_menor = lista.sort(reverse=True)
print(lista_mayor_menor)