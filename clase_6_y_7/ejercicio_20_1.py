pedidos_sandwiches = ["JYQ","Nutella","Completo"]
sandwiches_terminados = []
a = 0
while pedidos_sandwiches:
    print(f"se esta preparando el sandwich de {pedidos_sandwiches[a]}")
    sandwich_preparado = pedidos_sandwiches.pop(a)
    sandwiches_terminados.append(sandwich_preparado)
print(sandwiches_terminados)
    