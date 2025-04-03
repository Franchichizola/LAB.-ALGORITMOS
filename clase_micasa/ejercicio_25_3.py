def hacer_auto(fabricante, modelo, **info_extra):
    auto = {
        "fabricante": fabricante,
        "modelo": modelo,
    }
    for clave, valor in info_extra.items():
        auto[clave] = valor
    return auto

auto = hacer_auto("Toyota", "Corolla", color="gris", airbags=True)
print(auto)
