# Colas

#colas, estructura de datos de tipo FiFO

#al igual que con las pilas, se pueden simular las colas mediante listas, pero tambien se puede importar el modulo 'collections'; para este curso, se usaran listas

# from collections import deque

cola = ["Rafael", "Barbara", "Pedro","Muriel","Juan"]
#para agregar elementos, se agregan por el final
cola.append("Karla")
cola.append("Flor")
#para sacar elementos, se debe sacar el primer elemento de la lista
n = cola.pop(0)
print(n)