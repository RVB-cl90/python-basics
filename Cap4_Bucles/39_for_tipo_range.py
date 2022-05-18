#FOR tipo range
#es para especificar un numero determinado de repeticiones, sin usar una coleccion

for i in range(50):     #range crea, por asi decirlo, una coleccion ficticia de 50 elementos, en este caso, del 0 al 49
    print(f"{i}")

for i in range(5,11):     #de esta forma, range parte desde el 5 y llega hasta el (n-1)
    print(f"{i}")

for i in range(2,21,2):     #de esta forma, range parte desde el 2, llega hasta el (n-1) y avanza en intervalo de a 2
    print(f"{i}")