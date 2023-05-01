## program code
```python
"""
Durante la planificación de un proyecto se han acordado una lista de tareas.
Para cada una de estas tareas se ha asignado un orden de prioridad.
Cuanto menor es el número de oprden, más prioridad.
* Para ordenar automaticamente una lista es posible utilizar su metodo .sort()
"""
tareas = [
    [6, "Distribución"],
    [2, "Diseño"],
    [1, "Concepción"],
    [7, "Mantenimiento"],
    [4, "Producción"],
    [3, "Planificación"],
    [5, "Pruebas"],   
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
"""
Para resolver el programa vamos a crear una cola
"""
# Import deque
from collections import deque
# sort()
tareas.sort()
print(tareas)
print("Metodo sort()")
cola = deque()
for task in tareas:
    cola.append(task[1]) # task[1] para solo añadir el indice 1
    print(task, "Agregano a la cola")
print("\n==Tareas ordenadas==")
for task in cola:
    print(task)
    
# Para extraer la primera tarea a realizar
list_task_done = []
done_1= cola.popleft()
```

## output
```Bash
==Tareas desordenadas==
6 Distribución
2 Diseño
1 Concepción
7 Mantenimiento
4 Producción
3 Planificación
5 Pruebas
[[1, 'Concepción'], [2, 'Diseño'], [3, 'Planificación'], [4, 'Producción'], [5, 'Pruebas'], [6, 'Distribución'], [7, 'Mantenimiento']]        
Metodo sort()
[1, 'Concepción'] Agregano a la cola
[2, 'Diseño'] Agregano a la cola
[3, 'Planificación'] Agregano a la cola
[4, 'Producción'] Agregano a la cola
[5, 'Pruebas'] Agregano a la cola
[6, 'Distribución'] Agregano a la cola
[7, 'Mantenimiento'] Agregano a la cola

==Tareas ordenadas==
Concepción
Diseño
Planificación
Producción
Pruebas
Distribución
Mantenimiento

```

