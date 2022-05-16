# Listas - Parte 2

#semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#print(len(semana)) #imprime la cantidad de elementos dentro de la lista
'''
lista = [1,2,3,4,5]

lista.append(6) #agrega elementos al final de la lista
lista.append("Hola")

lista.insert(2,9) #funcion para insertar elemento a la lista en una posicion determina; primnero se indica la posicion en la que se va a insertar y despues que se va a insertar

lista.extend([7,8,0]) #funcion para agregar varios elementos a la lista, se concatena una lista indicada en la funcion al final de la lista inicial

print(lista)
'''
'''
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,1,1,1]

lista3 = lista1+lista2 #otra forma de concatenar listas

print(3 in lista3) #devuelve true si el valor preguntado esta en la lista
print(lista3.index(8)) #devuelve la posicion del indice donde se encuentra el elemento consultado en la lista, si no existe el elemento en la lista, devuelve error
print(lista3.count(1)) #devuelve la cantidad de veces que se repite el calor consultado en la lista
'''

lista = [1,2,3,4,5,"Hola","que","tal"]
lista2 = [9,4,8,3,6,-2,0,7,1]

lista.pop() #por defecto, elimina el ultimo elemento de la lista
lista.pop(6) #si se especifica un indice, elimina de la lista el valor en ese indice

lista.remove(4) #se especifica el valor del elemento que se quiere eliminar de la lista

#lista.clear() #se limpia la lista completa

lista.reverse() #se invierte el orden de los elementos de la lista

lista2.sort() #ordena los elementos de la lista en orden ascendente, solo para listas numericas
lista2.sort(reverse=True) #ordena los elementos de la lista en orden descendente

print(lista)
print(lista2)