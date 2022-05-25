#   Errores
#Se denomina errores a los cometidos por el programador

#errores de sintaxis, cuando falta un parentesis o como por ejemplo
print("Hola mundo"
#tambien, cuando por prisa se escribe mal el nombre de una funcion
prin("Hola mundo")
#En un condicional, bucle o funcion, cuando se olvidan los ':'
if 15 > 10
    print("es mayor")

#Errores semanticos, son errores en la logica de la ejecucion del codigo, por ejemplo
lista = [1,2,3]

lista.pop()
lista.pop()
lista.pop()
lista.pop()

#al tratar de eliminar mas elemtos de los que tiene la lista, se produce un "error de indice"
#otro ejemplo seria, tratar de acceder a un elemento que no existe dentro de una coleccion

print(lista[5]))

#otro tipo de error es cuando se pide ingresar datos, sin considerar el tipo de dato requerido

numero = input("Ingrese un numero: ")
print(f"la suma es: {numero+10}") #estro produce error, porque si en el comando 'input', no se especifica que se guarde como 'int', es considerado texto
