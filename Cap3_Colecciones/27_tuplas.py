# Tuplas
# Similar a una lista, pero no se puede modificar

tupla = (4,5,1,0,8,3,["Hola","mundo",4,7,8])

#tupla.append(5) # Esto da error, porque no se pueden agregar o eliminar valores a una tupla
# En las tuplas se pueden usar metodos de busqueda y de consulta
'''
print(tupla[-1])
print(4 in tupla)
print(tupla.index(4)) 
'''
# Una tupla se puede convertir en una lista y viceversa
lista = list(tupla)

tupla2 = tuple(lista)

print(lista)
print(tupla2)