import random

loteria = [3, 7, 12, 25, 44, 56, 60, 72, 81, 99, "A", "J", "L", "S", "T"]

ganador = random.sample(loteria, 4)

# Mostramos el mensaje
print(f"El boleto ganador es: \n {ganador}")
