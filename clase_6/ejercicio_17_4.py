ciudades = {
    "Londres": {
        "pais": "Reino Unido",
        "poblacion": 8982000,
        "dato_curioso": "Londres tiene el sistema de metro más antiguo del mundo, inaugurado en 1863."
    },
    "Paris": {
        "pais": "Francia",
        "poblacion": 2148000,
        "dato_curioso": "La Torre Eiffel fue inicialmente construida como una estructura temporal para la Exposición Mundial de 1889."
    },
    "Madrid": {
        "pais": "España",
        "poblacion": 6642000,
        "dato_curioso": "Madrid es la única capital europea que está situada a más de 300 kilómetros de la costa."
    }
}
for ciudad, info in ciudades.items():
    print(ciudad)
    for dato, cosas in info.items():
        print(f"{dato} : {cosas}")