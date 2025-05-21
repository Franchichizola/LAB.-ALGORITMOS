import random

loteria = [3, 7, 12, 25, 44, 56, 60, 72, 81, 99, "A", "J", "L", "S", "T"]


my_ticket = [7, "J", "A", 60]

intentos = 0
logrado = False

while not logrado:
    intentos += 1
    boleto = random.sample(loteria, 4)
    if boleto == my_ticket:
        logrado = True
        print(f"El boleto salio despues de {intentos} intentos.")
