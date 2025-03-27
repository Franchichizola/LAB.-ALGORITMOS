
a = True
respuesta = 0
cant_loop = 1
cant = int(input("Dime cuantas edades vas a ingresar"))
while cant_loop <= cant:
    cant_loop += 1
    respuesta = int(input("Dime tu edad (-1 para terminar)"))
    if respuesta != -1:
        if respuesta < 3:
            print("tu entrada es gratis")
        elif respuesta <= 12:
            print("tu entrada cuesta $10")
        elif respuesta > 12:
            print("tu entrada cuesta $15")
    else:
        break

print("siguiente programa")

respuesta = ""
ingredientes = []
cant_loop = 1
cant = int(input("Dime cuantos ingredientes vas a ingresar"))
while cant_loop <= cant:
    cant_loop += 1
    respuesta = input("Dime los ingredientes para la pizza (salir para terminar)")
    if respuesta.lower() != "salir":
        ingredientes.append(respuesta)
    else:
        break
    if cant_loop <= cant:
        for ingrediente in ingredientes:
            print(ingrediente)
for ingrediente in ingredientes:
   print(ingrediente)
