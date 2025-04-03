class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0
    
    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}\nTipo de cocina: {self.tipo_cocina}")
    
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

    def establecer_clientes_atendidos(self,numero):
        self.clientes_atendidos += numero
class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0
        self.sabores = ["ddl","vainilla","chocolate"]
    def mostrar_sabores(self):
        print("los sabores son")
        for sabor in self.sabores:
            print(sabor)
            
Puesto = PuestoDeHelados("Gelato", "Italiana")
Puesto.mostrar_sabores()
