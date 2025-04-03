class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}\nTipo de cocina: {self.tipo_cocina}")
    
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

restaurante1 = Restaurante("Ski-bidi Pizza", "Italiana")
restaurante2 = Restaurante("sang sung", "China")
restaurante3 = Restaurante("Parrillita", "Asado")

restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()

