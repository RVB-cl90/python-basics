# Multiples excepciones
# En el siguiente ejemplo, se presenta una funcion con distintos tipos de posibles excepciones
# Para ayudar al usuario, se puede especificar que tipo de excepcion resaltar

def dividir():
    while True:
        try:
            num1 = float(input("Digite un numero: "))
            num2 = float(input("Digite un numero: "))
            resultado = num1/num2
            print(f"El resultado de la division es: {resultado:.2f}")

        except ValueError:
            print("Error -> Digite correctamente los valores numericos.")

        except ZeroDivisionError:
            print("Error -> No se puede dividir por '0'.")
        else:
            break

dividir()