# Pilas

#no existe una estructura de pilas como tal en pyrhon, pero se pueden simular, con listas por ejemplo

pila = [1,2,3]
#a una pila se le agregan elementos por el final
pila.append(4)
pila.append(5)
#para sacar elementos de una pila, normalmente se quita primero el ultimo elemento, pila LIFO
#al quitar un elemento por el metodo 'pop', se devuelve el valor quitado

n = pila.pop()

print(n)
