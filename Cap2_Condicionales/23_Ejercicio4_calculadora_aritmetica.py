'''
Ejercicio 4:
Construir un programa que simule el funcionamiento de una calculadora que puede
realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación
y división). El usuario debe especificar la operación con el primer carácter
del nombre de la operación.

S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
'''

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

operacion = input("Indique la operacion a realizar: (Suma {S}, Resta {R}, Multiplicacion {M}, Division {D})").upper()

if len(operacion) == 1 and (operacion == 'S' or operacion == 'R' or operacion == 'M' or operacion == 'D'):
    if operacion == 'S':
        suma = num1+num2
        print(f"Resultado: {suma}")
    elif operacion == 'R':
        resta = num1-num2
        print(f"Resultado: {resta}")
    elif operacion == 'M':
        mult = num1*num2
        print(f"Resultado: {mult}")
    elif operacion == 'D':
        if num2 != 0:
            div = num1/num2
            print(f"Resultado: {div:.2f}")
        else:
            print("Error matematico, no se puede dividir por 0")
else:
    print("La operacion ingresada no es valida.")