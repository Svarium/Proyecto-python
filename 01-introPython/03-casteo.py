#Texto (str)

variable1 = "texto"
variable2 = "123456"
variable3 = "Texto123"


#numericas (int, float, complex)

variable4 = 10
variable5 = 2.5
variable6 = 1j

#Casteo de str a int
variablecasteada1 = int(variable2)

#Casteo de int a str
variablecasteada2 = str(variable4)

print(type(variablecasteada1))  # <class 'int'>
print(type(variablecasteada2))  # <class 'str'>

#tuppla a lista
variable7 = (1, 2, 3)
variable8 = list(variable7)

#lista a tupla
variable9 = [4, 5, 6]   
variable10 = tuple(variable9)