class Auto:
    """Un intento simple de representar un auto."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos para describir un auto."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def obtener_nombre_descriptivo(self):
        """Devuelve un nombre descriptivo bien formateado."""
        nombre_largo = f"{self.año} {self.marca} {self.modelo}"
        return nombre_largo.title()

class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria
    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")
    def obtener_autonomia(self):
        if self.capacidad_bateria == 40:
                rango = 150
        elif self.capacidad_bateria == 65:
                rango = 225
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")
    def actualizar_bateria(self):
        self.capacidad_bateria = 65

class AutoElectrico(Auto):
    """Representa aspectos de un auto, específicos de los vehículos eléctricos."""
    def __init__(self, marca, modelo, año):
        """        Inicializa los atributos de la clase padre.
        Luego inicializa los atributos específicos de un auto eléctrico.
        """
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()

auto = AutoElectrico(marca="si",modelo="2.18.7", año="1983 A.C")
auto.bateria.obtener_autonomia()
auto.bateria.actualizar_bateria()
auto.bateria.obtener_autonomia()