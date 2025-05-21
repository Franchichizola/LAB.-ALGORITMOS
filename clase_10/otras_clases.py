from clase_usuario import Usuario
class admin(Usuario):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = privilegios(["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"])
    def describir_privilegios(self):
        print(f"lista de privilegios:")
        self.privilegios.describir_privilegios()
        
class privilegios():
    def __init__(self,privilegio):
        self.privilegios = privilegio
    def describir_privilegios(self):
        for privilegio in self.privilegios:
            print(privilegio)