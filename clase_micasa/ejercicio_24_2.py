def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop(0)
        print(f"Enviando mensaje: {mensaje}")
        mensajes_enviados.append(mensaje)

mensajes = [
    "Hola, ¿cómo estás?",
    "Estoy",
    "Buen dia papu",
    "No",
    "Feliz cumple"
]

mensajes_enviados = []

enviar_mensajes(mensajes, mensajes_enviados)

print("Mensajes restantes:", mensajes)
print("Mensajes enviados:", mensajes_enviados)
