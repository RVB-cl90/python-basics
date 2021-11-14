#operadores logicos para obtener resultados booleanos
# and, or y not

#los operadores tienen un order: not -> and -> or

a = 10
b = 15
c = 20

res = ((a<b) and (b<c))

print (res)

res = ((a>b) and (b<c))

print (res)

res = ((a>b) or (b<c))

print (res)

res = not((a>b) or (b<c))

print (res)