#Conjuntos - Parte 2
#al crear un conjunto, la funcion "set" solo es necesaria para crear un conjunto vacio, si se le agregan elementos al crearlo, python ya lo reconoce como conjunto

a = {1,2,3}
b = {3,4,5}

# print(a == b) # devuelve false, porque los elementos de los conjuntos son diferentes
'''
c = a | b # simbolo "|" es la union de conjuntos
c = a & b # simbolo "&" es la interseccion de conjuntos
c = a - b # simbolo "-" es la diferencia de conjuntos
c = b - a # simbolo "-" es la diferencia de conjuntos
c = a ^ b # simbolo "^" es la diferencia simetrica de conjuntos
'''
c = {1,2,3,4,5}

#issubset(), consulta si un conjunto es subconjunto de otro
#issuperset(), consulta si un conjunto es superconjunto de otro
#isdisjoint(), consulta si un conjunto es disconexo de otro
#frozenset(), se usa al crear un conjunto para hacerlo inmutable, es decir, que no se pueda modificar

print(b.issubset(c))
print(c.issuperset(a))