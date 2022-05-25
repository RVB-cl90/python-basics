# Lanzar nuestras propias excepciones

# Se usa la palabra reservada 'raise', seguida de un tipo de error, seguido de un mensaje que podemos definir

def verificandoEdad(edad):
    if edad < 0:
        raise ValueError ("La edad no puede ser negativa")
    elif edad < 18:
        print("Eres muy joven")
    elif edad < 30:
        print("Eres joven")
    elif edad < 50:
        print("Eres maduro")

edad = int(input("Digite su edad: "))
try:
    verificandoEdad(edad)
except ValueError as EdadNegativa:
    print(EdadNegativa)

print("Programa terminado.")