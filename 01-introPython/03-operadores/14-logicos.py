#OPERADORES LOGICOS

#and - funciona para evaluar si ambas condiciones son verdaderas

#or - funciona para evaluar si al menos una de las condiciones es verdadera

#not - funciona para invertir el valor de una condición (si es True, lo convierte en False, y viceversa)

x = 15
y = 20

booleano = (x > 3) and (x < 10)  # True, porque ambas condiciones son verdaderas

print(booleano)

booleano = (x > 3) or (x < 10)  # True, porque al menos una condición es verdadera

print(booleano)

booleano = not (x == 3)  # True, porque x no es igual a 3, por lo tanto not invierte el valor a True

print(booleano)

a = x > y  # esto es False, porque 15 no es mayor que 20
b = y > x  # esto es True, porque 20 es mayor que 15

booleano = not (a and b) # not invierte el valor de la expresión a and b, que es False, por lo tanto se convierte en True
print(booleano)  # Imprime True, porque not(False) es True