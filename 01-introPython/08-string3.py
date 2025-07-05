#Concatenación de strings

a = "Hola"
b = "Python"
c = a + " " + b

print(c)

texto = "El contenido de este curso va a durar {} horas y tendrá {} clases"
horas = 20
clases = 50

print(texto.format(horas, clases))  # Imprime "El contenido de este curso va a durar: 20 horas"


# Concatenación de strings con f-strings
texto_f = f"El contenido de este curso va a durar {horas} horas y tendrá {clases} clases"
print(texto_f)  # Imprime "El contenido de este curso va a durar: 20 horas y tendrá 50 clases"



texto2 = "La mejor serie de la historia es \"Breaking Bad\""
print(texto2)  # Imprime "La mejor serie de la historia es 'Breaking Bad'"

texto3 = "La carpeta donde esta mi trabajo es C:\\Users\\Usuario\\Documents"
print(texto3)  # Imprime "La carpeta donde esta mi trabajo es C:\Users\Usuario\Documents"

texto4 = "La mejor serie de la historia es: \n 'Breaking Bad'" # \n es un salto de línea
print(texto4)  # Imprime "La mejor serie de la historia es: 'Breaking Bad'" con salto de línea

texto5 = "La mejor serie de la historia es: \t 'Breaking Bad'" # \t es un tabulador
print(texto5)  # Imprime "La mejor serie de la historia es: 'Breaking Bad'" con tabulador