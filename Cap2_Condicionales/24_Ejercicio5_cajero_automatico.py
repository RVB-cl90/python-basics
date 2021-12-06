'''
Ejercicio 5:
Hacer un programa que simule un cajero automático con un saldo inicial de $1000
y tendrá el siguiente menú de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

saldo = int(1000)

print("\tBienvenido a su cajero automatico. \n\n \tSeleccione la operacion a realizar.\n")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar saldo disponible")
print("4. Salir")

operacion =  int(input("Indique la operacion a realziar: "))

if 0 < operacion < 5:
    if operacion == 1:
        abono = int(input("Indique la cantidad a ingresar."))
        if abono > 0:
            saldo += abono
            print(f"Se han abonado ${abono} a su cuenta, su nuevo saldo es ${saldo}")
        else:
            print("No se puede abonar un valor negativo.")
    elif operacion == 2:
        retiro = int(input("Indique la cantidad a retirar."))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Se han retirado ${retiro} de su cuenta, su nuevo saldo es ${saldo}")
            else:
                print("Excede el valor de su saldo disponible.")
        else:
            print("No se puede retirar un valor negativo.")
    elif operacion == 3:
        print(f"Su saldo actual es de ${saldo}")
    else:
        print("Hasta luego.")
else:
    print("Operacion invalida.")