'''
Usos de
- if
- else
- elif
'''

a = 5
b = 10
if a == 5:
    print("a vale:", a)
    if b == 10:
        print("y b vale:", b)

'''
Ejemplo 2
'''
c = 5
d = 10
if c == 5 and d == 10:
    print("c vale 5 y d vale 10")

'''
Else / Elif
Determinar si es un numero par o impar
'''

n = 10
if n % 2 == 0:
    print(n, "es un nunmero par")
else:
    print(n, "es un nunmero impar")

'''
Creando un comando con elif
'''
print("Ejemplo de un comando con elif")
comando = "Salir"
if comando == "Entrar":
    print("Bienvenido al sistema")
elif comando == "Saludar":
    print("Hola, espero que te lo estés pasando bien aoprndiendo python")
elif comando == "Salir":
    print("Saliendo del sistema")
else:
    print("Comando no reconocido")

'''
Creando un programa para revisar notas
'''
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("notable")
elif nota >=6:
    print("Bien")
elif nota >=5:
    print("Suficiente")
else:
    print("Insuficiente")

