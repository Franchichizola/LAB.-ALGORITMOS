a = True
respuesta = 0
while respuesta != -1:
    respuesta = int(input("Dime tu edad (-1 para terminar)"))
    if respuesta != -1:
        if respuesta < 3:
            print("tu entrada es gratis")
        elif respuesta <= 12:
            print("tu entrada cuesta $10")
        elif respuesta > 12:
            print("tu entrada cuesta $15")
