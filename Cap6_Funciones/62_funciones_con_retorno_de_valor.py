#   Funciones con retorno de valor
#la unica diferencia es que estas funciones devuelven un valor, el que debe ser almacenado o usado; en caso contrario, el resultado quedara en el aire

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

resultado = multiplicar(3,4)

print(f"\nEl resultado de la multiplicacion es: {resultado}")

#tambien es posible hacer que una funcion retorne multiples valores, para ello, se deben especificar una variable por cada valor retornado.

def multiple_retorno():
    return "Hola",53,[1,2,3,4,5]

c,n,l = multiple_retorno()
print(c)
print(n)
print(l)