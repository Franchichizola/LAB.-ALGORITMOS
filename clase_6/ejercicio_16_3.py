lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas_a_encuestar = ["Pepe","Juan","Eduardo","Maria","Emma"]
for persona in lenguajes_favoritos.keys():
    if persona in personas_a_encuestar:
        print("Gracias por responder la encuesta skibidi", persona)
    if persona not in personas_a_encuestar:
        print(f"Hola {persona} por favor responde la encuesta 🙄")
    