#-- TIPOS DE DATOS --

#---------
#TEXTO:
#---------

#String (str) - cadenas de texto
nombre = "Juan"

#-------------
#NUMÉRICOS
#-------------

# - Enteros (int):
edad = 30

# - Flotantes (float):
altura = 1.75

# - Complejos (complex):
numero_complejo = 2 + 3j

#-------------
#SECUENCIAS
#-------------

# - Listas(List - ordenada y mutable)
lista = [1, 2, 3, "cuatro", 5.0]

# - Tuplas (Tuple - ordenada e inmutable)
tupla = (1, 2, 3, "cuatro", 5.0)

# - Rangos (range - secuencia inmutable de números)
rango = range(0, 10)  # del 0 al 9

#-------------
#MAAPPING TYPE (MAPEO)
#-------------

# - Diccionario (dict - colección de pares clave-valor)
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "altura": 1.75
}

#-------------
#SET TYPES (CONJUNTOS)
#-------------

# - set (set - colección no ordenada y mutable de elementos únicos)
conjunto = {1, 2, 3, 4, 5}

# - frozenset (frozenset - colección no ordenada e inmutable de elementos únicos)
conjunto_inmutable = frozenset({1, 2, 3, 4, 5})

#-------------
#SET TYPES (CONJUNTOS)
#-------------

# - Booleanos (bool - True o False)
es_mayor_de_edad = True

#-------------
#BINARY TYPES (TIPOS BINARIOS)
#-------------

# - bytes (bytes - secuencia inmutable de bytes)
datos_binarios = b"Hola, mundo"

# - bytearray (bytearray - secuencia mutable de bytes)
datos_binarios_mutable = bytearray(b"Hola, mundo")

# - memoryview (memoryview - vista de memoria de un objeto de bytes)
datos_memoryview = memoryview(datos_binarios)

#-------------
#NONE/NULL (NULO)
#-------------

# - None (NoneType - representa la ausencia de valor)
valor_nulo = None