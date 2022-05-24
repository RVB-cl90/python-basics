#   Argumentos por valor o por referencia

def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 5
doblar_valor(n)    #esto es el paso de argumento por valor, se pasa una copia del valor definido

def doblar_valor_2(numero):
    return numero * 2

n = 5
n = doblar_valor_2(n) #esto tambien es el paso de argumento por valor
print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2

n = [5,10,15,20]
doblar_valores(n)   #las colecciones se pasan por referencia, pero de manera similar, se pueden pasar por valor, usando el indice [:]
print(n)
