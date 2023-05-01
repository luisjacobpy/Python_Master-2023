class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        # Para devolver un mensaje
        print(f"Se ha creado la película: {self.titulo}")

    # Destructor de clase
    def __del__(self):
        print(f"Se esta borrando la pelicula: {self.titulo}")
        
    # Redefinimos el metodo string
    def __str__(self):
        return (f"lanzada en {self.lanzamiento} con una duracion de {self.duracion} minutos")
    
    # Redefinimos (len) 
    def __len__(self):
        return self.duracion
    
# Creamos eu objeto
p = Pelicula("El padrino", 175, 1972) # Se ha creado la película: El padrino
print(str(p)) # lanzada en 1972 con una duracion de 175 minutos
print(len(p)) # 175
del(p) # Se esta borrando la pelicula: El padrino
