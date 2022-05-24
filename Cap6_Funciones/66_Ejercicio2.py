'''
Ejercicio 2: Hacer un programa que pida la anchura y altura de un
rectángulo y con ayuda de una función lo dibuje con *.
'''
'''
def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()


ancho = int(input("Digite el ancho: "))
alto = int(input("Digite el alto: "))

print()
dibujar(ancho,alto)
'''

def dibujo(alto,ancho):
    for i in range(alto):
        for j in range(ancho):
            print("-",end="")
        print()
print("\tDibujo de rectangulo.\n")
alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
print()
dibujo(alto,ancho)
