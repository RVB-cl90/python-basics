#Conjuntos#Conjuntos
#Grupos de elementos que se agregan de forma desordenada, y se caracterizan en que no pueden haber duplicados

conjunto = set()

#conjunto = {} #Conjuntos se pueden inicializar con llaves, pero asi tambien se definen los diccionarios, y python les da prioridad
#NO PUEDE HABER OTRO TIPO DE COLECCIONES DENTRO DE UN CONJUNTO

conjunto = {1,2,3,4,5,6,7,1,2,3} #ignora los valores duplicados

conjunto.clear()

conjunto.add(0)
conjunto.add(12)
conjunto.add("Hola")
conjunto.add("B")
conjunto.add(-1)

conjunto.discard(3)
conjunto.discard("Hola")


print(conjunto)

print(0 in conjunto)

