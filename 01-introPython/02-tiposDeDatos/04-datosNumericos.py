x=1 #int
y=2.5 #float
z=1j #complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>   
print(type(z))  # <class 'complex'>

#CASTEO DE TIPOS NUMERICOS

variable1 = 5

variableCasteada1 = float(variable1)  # int a float
print(variableCasteada1)  # 5.0

variable2 = 3.14
variableCasteada2 = int(variable2)  # float a int
print(variableCasteada2)  # 3

variable3= 2j
#variableCasteada3 = int(variable3)  # complex a int
# print(variableCasteada3)  # TypeError: can't convert complex to int

