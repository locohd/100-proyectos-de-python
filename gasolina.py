# Este es el programa 9 de la lista de proyectos de Python
# Este programa simula una gasonileria el usuario ingresa los litros de la gasolina y imprime el total de litros y el total del pago
# El programa calcula si ya pago completo o si le falta el pago de la gasolina y si da de mas le regresa el cambio
premium = 28.99
magna = 23.99
tipo = input("Ingresa el tipo de gasolina (premium/magna): ").lower()

if tipo == "magna":
    precio = magna
    print("Gasolina magna.")
elif tipo == "premium":
    precio = premium
    print("Gasolina premium.")
else:
    print("Tipo de gasolina no válido.")
    exit()

print(f"Precio por litro: ${precio:.2f}")
litros = float(input("Ingresa la cantidad de litros: "))
total = litros * precio
restante = total
print(f"Total de litros: {litros}L, total a pagar: ${total:.2f}")

while restante > 0:
    monto = float(input(f"Ingresa el monto a pagar ${restante:.2f} restantes: "))
    restante -= monto

    if restante > 0:
        print(f"Falta pagar: ${restante:.2f}")
    elif restante < 0:
        print(f"Te sobra: ${-restante:.2f}")

print("Pago completo, gracias por su compra.")

    