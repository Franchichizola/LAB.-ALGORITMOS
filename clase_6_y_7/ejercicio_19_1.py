respuesta = ""
ingredientes = []
while respuesta.lower() != "salir":
    respuesta = (input("Dime los ingredientes para la pizza (salir para terminar)"))
    if respuesta.lower() != "salir":
        ingredientes.append(respuesta)
    for ingrediente in ingredientes:
        print(ingrediente)

