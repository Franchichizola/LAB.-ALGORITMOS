def construir_perfil(nombre, apellido, **info_usuario):
    perfil = {
        "nombre": nombre,
        "apellido": apellido,
    }
    for clave, valor in info_usuario.items():
        perfil[clave] = valor
    return perfil

mi_perfil = construir_perfil(
    "Franco", "Chichizola",
    edad=16,
    profesion="Estudiante",
    ciudad="Buenos Aires"
)

print(mi_perfil)
