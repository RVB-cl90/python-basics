# Listas

lista = [] #creacion de lista vacia

print(lista)

semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

print(semana) #imprime la lista completa

print(semana[0]) # imprime solo el elemento indicado por el indice, desde 0 hasta n-1

print(semana[-1]) #con indice negativo, es similar a acceder a la lista desde el ultimo elemento

'''print(semana[7])''' #con un indice mayor a la cantidad de elementos, se produce una excepcion de tipo "IndexError"

print(semana[2:5]) #de esta forma, se imprimen sublistas; desde el elemento 2, se imprime hasta la posicion 5; se se deja vacio despues de los ":", imprime hasta el final de la lista