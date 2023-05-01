# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
]



# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return

    print('Cliente no encontrado')  
    
# llamamos a la funcion
borrar_cliente(clientes, '22222222V')  # Cliente no encontrado
borrar_cliente(clientes, '22222222B') # {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'} > BORRADO

# Revisamos la lista
print(clientes) # [{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}]
# Ya no aparece dentro de la lista el elemento eliminado.
