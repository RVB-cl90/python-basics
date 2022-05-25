#   Funciones Recursivas

def cuenta_regresiva(num):
    if num > 0:
        print(num)
        cuenta_regresiva(num-1)
    else:
        print("BOOM")

cuenta_regresiva(10)
#   Funcion recursiva, es aquella que se llama a si misma, bajo cierta condicional, para evitar bucles infinitos