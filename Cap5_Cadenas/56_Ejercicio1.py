# Ejercicio 1 - Cadena más larga
'''
cadena1 = input("Digite una cadena: ")
cadena2 = input("Digite otra cadena: ")

if len(cadena1) > len(cadena2):
    print(f"\nLa cadena más larga es: {cadena1}")
elif len(cadena2) > len(cadena1):
    print(f"\nLa cadena más larga es: {cadena2}")
else:
    print("\nAmbas cadenas son iguales en longitud")
'''

cadena1 = input("Ingrese una palabra y/o cadena: ")
cadena2 = input("Ingrese otra palabra y/o cadena: ")

if len(cadena1) > len(cadena2):
    print(f"La cadena más larga es: {cadena1} \n")
elif len(cadena2) > len(cadena1):
    print(f"La cadena más larga es: {cadena2} \n")
else:
    print("Ambas cadenas tienen igual longitud\n")