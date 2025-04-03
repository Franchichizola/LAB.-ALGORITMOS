class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def describir_usuario(self):
        print(f"Usuario\nNombre: {self.nombre}\nApellido: {self.apellido}")
    
    def saludar_usuario(self):
        print(f"Hola skibidi {self.nombre} {self.apellido} 🐧.")

usuario = Usuario("Jorgito", "Uchiha")
usuario.describir_usuario()
usuario.saludar_usuario()
