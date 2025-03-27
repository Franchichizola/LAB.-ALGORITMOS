lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas_a_encuestar = ["Pepe","Juan","Eduardo","Maria","Emma"]
for persona in personas_a_encuestar:
    if persona in lenguajes_favoritos.keys():
        print("Gracias por responder la encuesta skibidi", persona)
    if persona not in lenguajes_favoritos.keys():
        print(f"Hola {persona} por favor responde la encuesta 🙄")
    