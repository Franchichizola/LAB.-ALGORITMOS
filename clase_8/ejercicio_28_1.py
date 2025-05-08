class Restaurante():
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

restaurante = Restaurante("Ski-bidi Pizza", "Italiana")
restaurante.clientes_atendidos = 3
print(restaurante.clientes_atendidos)
restaurante.establecer_clientes_atendidos(5)
print(restaurante.clientes_atendidos)