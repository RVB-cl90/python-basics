# Condicionales Combinados

edad = int(input("Digite su edad: "))

'''
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
'''
'''if edad > 0 and edad < 100:'''
if 0 < edad < 100:
    print("Edad valida")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("Valor invalido para ser edad")

# considerando que una persona no puede tener su edad con valor negativo
# y que tampoco supera los 100 años de edad