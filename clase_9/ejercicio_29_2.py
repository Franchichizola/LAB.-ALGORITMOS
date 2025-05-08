class Usuario():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def describir_usuario(self):
        print(f"Usuario\nNombre: {self.nombre}\nApellido: {self.apellido}")

class admin(Usuario):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]
    def describir_privilegios(self):
        print(f"lista de privilegios:")
        for privilegio in self.privilegios:
            print(privilegio)
administrador = admin(nombre="pepe", apellido="dominguez")

administrador.describir_usuario()
administrador.describir_privilegios()