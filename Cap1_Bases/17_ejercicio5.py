# Una tienda ofrece el 15% de descuento, un cliente desea saber cuanto debera pagar al final por su compra

compra = float(input("Ingrese el valor de su compra: "))

precio_final = round((compra * 85)/100)

print(f"El cliente debe pagar: ${precio_final}")