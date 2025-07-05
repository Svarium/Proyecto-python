#Metodos de cadenas de caracteres

txt = "hola, estoy aprendiendo metodos de cadenas de caracteres"

numeros = "1234567890"

print(txt.capitalize())  # Imprime "Hola python" (primera letra en mayúscula)
print(txt.title())  # Imprime "Hola, Estoy Aprendiendo Metodos De Cadenas De Caracteres" (cada palabra en mayúscula)
print(txt.center(100, '*'))  # Imprime "****hola, estoy aprendiendo metodos de cadenas de caracteres****" (centra el texto con asteriscos)
print(txt.count('a'))  # Imprime 5 (número de veces que aparece 'a')
print(txt.endswith('caracteres'))  # Imprime True (verifica si termina con 'caracteres')
print(txt.find('aprendiendo'))  # Imprime 12 (posición de la subcadena 'aprendiendo')
print(numeros.isdigit())  # Imprime True (verifica si todos los caracteres son dígitos)
print(txt.islower())  # Imprime True (verifica si todos los caracteres están en minúsculas)
print(txt.isupper())  # Imprime False (verifica si todos los caracteres están en mayúsculas)