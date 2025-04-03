def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones:
        album['canciones'] = canciones
    return album

print(hacer_album("Pink Floyd", "The Dark Side of the Moon"))
print(hacer_album("Nirvana", "Nevermind"))
print(hacer_album("The Beatles", "Abbey Road"))

album_con_canciones = hacer_album("Queen", "A Night at the Opera", 12)
print(album_con_canciones)
