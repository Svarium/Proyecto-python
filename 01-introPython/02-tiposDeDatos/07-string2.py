#slicing: ponemos desde un indice hasta otro no incluido
# podemos usar slicing para obtener una parte de un string

text = "seguimos trabajando con strings"
print(text[:8]) # Imprime "seguimos"
print(text[9:19])  # Imprime "trabajando"
print(text[-7:])  # Imprime "strings"


text2 = "ESCRIBO EN MAYUSCULAS GRITANDO"
print(text2.lower())  # Convierte todo a minúsculas

text3 = "escribo en minusculas susurrando"
print(text3.upper())  # Convierte todo a mayúsculas

text4 = "   Hola, Python!   "
print(text4.strip())  # Elimina espacios al inicio y al final