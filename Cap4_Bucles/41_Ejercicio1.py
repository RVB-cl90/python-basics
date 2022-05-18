# Ejercicio 1 - Llenar una lista con los números del 1 al 50 y mostrarlos


# Agregamos a la lista los elementos del 1 al 50
lista = []
i=1
while i<=50:
    lista.append(i)
    i+=1
#metodo alternativo para llebar la lista
#   lista = list(range(1,51))


# Imprimiendo los elementos de la lista
for i in lista:
    if i < 50:
        print(i,end="-")
    else:
        print(i)