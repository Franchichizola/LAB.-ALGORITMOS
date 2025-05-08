class Usuario():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_login = 0
    
    def describir_usuario(self):
        print(f"Usuario\nNombre: {self.nombre}\nApellido: {self.apellido}")
    
    def saludar_usuario(self):
        print(f"Hola skibidi {self.nombre} {self.apellido} 🐧.")
    def incrementar_intentos_login(self):
        self.intentos_login += 1
    
    def reiniciar_intentos_login(self):
        self.intentos_login = 0     

usuario = Usuario("Jorgito", "Uchiha")
usuario.describir_usuario()
usuario.saludar_usuario()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
print(usuario.intentos_login)
usuario.reiniciar_intentos_login()
print(usuario.intentos_login)