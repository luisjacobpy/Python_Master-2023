pila = [3,4,5]
## Adding
pila.append(6)
pila.append(7)

## Sacar elementos
pila.pop() # Sacamos el ultimo elemento
print(pila)
# Si queremos guardar el elemenoto que sacamos de la fila
n = pila.pop()
print(n)

# Importamos el modulo de cola
from collections import deque
cola = deque()
print(cola)

cola = deque(['Hector','Juan','Miguel'])
print(cola)
# Agregamos elementos
cola.append('Maria')
cola.append('Fernando')
print(cola)
# Sacar elementos de la cola
# Metodo popleft
person_delete = cola.popleft() # Guardo la persona que quite

print(person_delete)
print(cola)
