'''
Ejercicio 3:
Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de
insertar. Por último, muestra los números ordenados de menor a mayor
'''

lista = []
numero = int(input("\nInserte un valor numerico (dejara de pedirle cuando inserte un 0): "))

while numero != 0:
    lista.append(numero)
    numero = int(input("\nInserte un valor numerico (dejara de pedirle cuando inserte un 0): "))

print("La lista de numeros ingresados, de forma ordenada es: ")
lista.sort()
for i in lista:
    print(i,end='-')

# metodo optimo para imprimir la lista

print(f"\n{lista}")