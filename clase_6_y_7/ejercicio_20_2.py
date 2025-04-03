pedidos_sandwiches = ["pastrón","pastrón","pastrón","JYQ","Nutella","Completo"]
sandwiches_terminados = []
print("hola mi gente nos quedamos sin pastrón 😭")
a = 0
while pedidos_sandwiches:
    if pedidos_sandwiches[a] != "pastrón":
        print(f"se esta preparando el sandwich de {pedidos_sandwiches[a]}")
        sandwich_preparado = pedidos_sandwiches.pop(a)
        sandwiches_terminados.append(sandwich_preparado)
    else:
        del pedidos_sandwiches[a]
print(sandwiches_terminados)
    