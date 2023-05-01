"""
Para poder sacar el identificador del codigo que no sarrroja el error
"""
try:
    n = int(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena ")
except ValueError:
    print("Debes introducir un acadena que sea un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print( type(e).__name__)