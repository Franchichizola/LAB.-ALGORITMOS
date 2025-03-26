glosario = {
    "Variable": "Una ubicación de almacenamiento que tiene un nombre simbólico (un identificador) y está asociada con un valor o información.",
    "Función": "Un bloque de código reutilizable que realiza una tarea específica y se ejecuta cuando se le invoca.",
    "Bucle": "Una estructura de control que repite un bloque de código mientras se cumpla una condición determinada.",
    "Lista": "Una colección ordenada de elementos que puede contener elementos de diferentes tipos, como números, cadenas de texto, entre otros.",
    "Diccionario": "Una estructura de datos que almacena pares de clave-valor, donde cada clave es única y se asocia con un valor."
}
for palabra, significado in glosario.items():
    print(f"{palabra}\n es {significado}")