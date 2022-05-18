# FOR
#en python, se usa con colecciones

for i in [1,2,3,4,5,"Pedro"]:   #palabra reservada del sistema 'for', un iterador 'i', en <-> 'in' una coleccion
    print(i)

#se ejecuta lo que este en el interior del 'for' por la cantidad de elementos que tenga la coleccion

coleccion = [1,2,3,4,5,"Pedro"]         #usando una lista
for i in coleccion:
    print(i)

coleccion = (1, 2, 3, 4, 5, "Pedro")    #usando una tupla
for i in coleccion:
    print(i)

coleccion = {1, 2, 3, 4, 5, "Pedro"}    #usando un conjunto
for i in coleccion:
    print(i)

coleccion = {"Pedro":22,"Maria":25,"Jose":30,"Luis":40}         #En un diccionario, si se especifica solo el elemento iterador, el valor mostrado sera el de la clave del diccionario
for i in coleccion:                                             #para mostrar el valor del diccionario, se debe especificar el nombre de la coleccion y el iterador como indice
   print(coleccion[i])
#otra forma de hacerlo es
for clave,valor in coleccion.items():                                             #para mostrar el valor del diccionario, se debe especificar el nombre de la coleccion y el iterador como indice
   print(f"{clave} -> {valor}")

#tambien se puede usar el for para recorrer una cadena
coleccion = "Rafael"
for i in coleccion:
    #print(f"{i}")   #se imprime letra por letra
    print(f"{i}",end=" ")   #agregando el 'end' en el 'print', podemos evitar el salto de linea despues de imrpimir cada letra