# Ejercicio 1 - Eliminar los elementos repetidos de una lista
'''
lista = [1,2,3,"Alejandro",2,2,1,"Alejandro",3]

lista = list(set(lista))

print(lista)
'''

lista = [1,2,3,3,4,2,2,"Rafael",1,1,1,3,5,"Rafael"]

conjunto = set(lista)

lista = list(conjunto)

print(lista)