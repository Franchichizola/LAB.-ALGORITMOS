class Usuario():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def describir_usuario(self):
        print(f"Usuario\nNombre: {self.nombre}\nApellido: {self.apellido}")

