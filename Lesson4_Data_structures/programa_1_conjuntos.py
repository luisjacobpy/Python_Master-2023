"""
Programa 1 - Colecciones de datos
 * Realiza un programa que siga las siguientes instrucciones
 1) Crea un conjunto llamado usuarios con los usuarios: Maria, David, Elvira, Juan y Marcos.
 2) Crea un conjunto llamado administradores con los administradores Juan y Maria
 3) Borra al administrador 'Juan' del conjunto de administradores.
 4) Añade a 'Marcos' como un nuevo administrador, pero no lo borres del conjunto de usuarios.
 5) Muestra a todos los usuarios de forma dinamica ademas de mostrar si es administrador o no.

"""
# 1 - usuarios
usuarios = {"Maria", "David", "Elvira", "Juan", "Marcos"}

# 2- administradores

administradores = {"Juan","Maria"}
# Tambien se puede usar remove
administradores.discard("Juan")

# 3 Añadir administrador
administradores.add("Marcos")

print(f"""
Los usuarios son:
{usuarios} 
""")

print(f"""
Los administradores son:
{administradores} 
""")

# 4
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "NO es admin")
