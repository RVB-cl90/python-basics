# Ejercicio 3 - Palabra o frase palíndroma
'''
cadena = input("Digite una cadena: ")

# Primero, quitamos los espacios en blanco de la cadena
cadena = cadena.replace(" ","")

# Segundo, invertimos la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("La cadena es un palíndromo")
else:
    print("La cadena NO es un palíndromo")
'''

cadena = input("Ingrese una palabra o frase para validar si es un palindromo: ")

cadena = cadena.replace(' ','')

cadena2 = cadena[::-1]  #   metodo para onvertir una cadena

if cadena == cadena2:
    print("\nLa cadena ingresada es un palindromo.")
else:
    print("\nLa cadena ingresada no es un palindromo.")
