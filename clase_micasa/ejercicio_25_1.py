def hacer_sandwich(*ingredientes):
    print("ingredientes:")
    for ingrediente in ingredientes:
        print(f"{ingrediente}")

# Llamadas a la función con diferentes cantidades de ingredientes
hacer_sandwich("jamón", "queso", "lechuga")
hacer_sandwich("pollo", "tomate")
hacer_sandwich("atun", "mayonesa", "huevo", "cebolla", "aceitunas")
