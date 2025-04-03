usuarios_actuales = ["Xx_juancitoGamer_xX", "PepitoYT", "Ivan777","MrDododie", "Mario"]
usuarios_nuevos = ["Xx_juancitoGamer_xX", "JorgitoMC", "Ivan777","Marqui", "Ayaleco"]
usuarios_actuales_minuscula = []
for usuario in usuarios_actuales:
    usuarios_actuales_minuscula.append(usuario.lower())
for nombre_usuario_nuevo in usuarios_nuevos:
    if nombre_usuario_nuevo.lower() in usuarios_actuales_minuscula:
        print("el usuario", nombre_usuario_nuevo, "ya esta en uso")
    else:
        print("el usuario", nombre_usuario_nuevo, "ya no esta en uso") 
            
    
