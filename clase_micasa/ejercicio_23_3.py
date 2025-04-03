def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones:
        album['canciones'] = canciones
    return album

print(hacer_album("Pink Floyd", "The Dark Side of the Moon"))
print(hacer_album("Nirvana", "Nevermind"))
print(hacer_album("The Beatles", "Abbey Road"))
print(hacer_album("Queen", "A Night at the Opera", 12))
a = 0
seguir = ""
while True:
    print("Ingresá los datos del álbum")
    if a >= 1:
        seguir = input("Deseas ingresar otro album? (si/no)")
    if seguir.lower() == "no":
        break
    elif seguir.lower()== "si" or a == 0:
        artista = input("Nombre del artista: ")
        
        titulo = input("Título del álbum: ")
        
        canciones = input("Cantidad de canciones: ")
        a += 1
        album_usuario = hacer_album(artista, titulo, canciones)
        print("\nÁlbum creado:", album_usuario)
    else:
        print("Error")

