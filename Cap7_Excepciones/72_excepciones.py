#   Excepciones
# las excepciones se producen por la interaccion del usuario con el codigo
'''
numero = int(input("Digite un numero: "))

print(f"La suma es: {numero+10}")
'''
#En el ejemplo anterior, logicamente no hay error, pero al momento de ingresar el numero, el usuario puede tratar de ingresar un numero escribiendolo, es decir 'uno', 'dos', etc
#Al ocurrir una excepcion, la ejecucion del programa se detiene, si hubiera mas codigo, no se ejecutaria

#Para manejar las excepciones, se usan las palabras reservadas 'try' y 'except'

while True:
    try:
        numero = int(input("Digite un numero: "))
        print(f"La suma es: {numero+10}")
    except:
        print("Ha ocurrido un error")
    else:       #el 'else', se ejecuta si no ocurre una excepcion
        print("Programa finalizado correctamente")
        break
    finally:    #el 'finally' se ejecutara siempre, en casao de excepcion o no
        print("Iteracion finalizada")

print("Programa terminado")