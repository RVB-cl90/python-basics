# While
#codigo que se repite bajo ciertas condiciones; un loop

import math

numero = int(input("Digite un numero positivo: "))

while numero < 0:      #while es una palabra reservada del lenguaje, por eso cambia de color, luego la condicion que devuelva true o false y ":" para pasar al cuerpo del while
    print("Error, el numero ingresado debe ser mayor o igual a 0")
    numero = int(input("Digite un numero positivo: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")