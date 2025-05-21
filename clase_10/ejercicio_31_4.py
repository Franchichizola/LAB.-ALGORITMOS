import difflib

texto1 = "pepe"
texto2 = "Pepe!"

diferencias = difflib.ndiff(texto1, texto2)
print('\n'.join(diferencias))
