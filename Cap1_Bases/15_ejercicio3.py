#Intercambiar el valor de dos variables

a = float(input("Ingrese un valor para la variable 'a': "))
b = float(input("Ingrese un valor para la variable 'b': "))

c = a
a = b
b = c

#una forma mas sencilla de hacerlo es 'a , b = b , a'
#esto indica que el valor de a debe ser b y b debe ser a

print(f"Al cambiar el valor de las variables a = {a} y b = {b}")