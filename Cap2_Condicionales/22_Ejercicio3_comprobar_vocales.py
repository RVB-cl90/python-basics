'''
Ejercicio 3:
Hacer un programa que pida un carácter e indique si es una vocal o no.
'''

letra = input("Digite un caracter: ").lower()

if len(letra) < 1:
    print("Debe ingresar un caracter")
elif len(letra) > 1:
    print("Debe ingresar solo un caracter")
else:
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        print("Es una vocal")
    else:
        print("No es una vocal")