# Ingresar el radio de un circulo y devolver su area y su circunferencia

radio = float(input("Ingrese el radio del circulo: "))

area = 3.1416*radio**2
circunferencia = 2*3.1416*radio

print(f"El Area es: {area} y su curcunferencia es : {circunferencia} ")

#adicionalmente, en vez de usar el valor '3.1416' para "Pi", se puede importar un modulo matematico que contenga el valor de "Pi"

'''
import math

area = math.pi * radio**2
circunferencia = 2*math.pi*radio

'''

#para acortar la cantidad de decimales que muestra un flotante al imprimir el valor de una variable, ' {area:.2f}', esto indica que despues del valor entero, mostrara solo dos decimales