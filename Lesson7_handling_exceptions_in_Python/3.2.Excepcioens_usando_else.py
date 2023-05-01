"""
En el siguiente programa usamos try and except en el codigo propoenso a errores.
Se utiliza el 'while' para volver a solicitar valores en caso de que el valor inicial no sea el esperado.
Se utiliza 'else' que se ejecuta en caso de que no se ejecute el 'except'.
"""

while(True):
    try: 
        n = float(input("Introduce un numero: "))
        m = 4
        print(f"{n}/{m} = {n/m}")
        
    except:
        print("Ha ocurrido un error introduce bien el numero")
        
    else:
        print("Todo ha funcionado correctamente")
        break # Importante romper la iteracion si  todo ha salido bien