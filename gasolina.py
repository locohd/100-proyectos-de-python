# Este es el programa 9 de la lista de proyectos de Python
# Este programa simula una gasonileria el usuario ingresa los litros de la gasolina y imprime el total de litros y el total del pago
# El programa calcula si ya pago completo o si le falta el pago de la gasolina y si da de mas le regresa el cambio
premium = 28.99
magna = 23.99
tipo = input("Ingresa el tipo de gasolina (premium/magna): ").lower()

if tipo == "magna":
    print(f"Gasolina magna.")
    print(f"Precio por litro: ${magna:.2f}")
    litros = float(input("Ingresa la cantidad de litros: "))
    total = litros * magna
    print(f"Total de litros: {litros}, total a pagar: ${total:.2f}")

elif tipo == "premium":
    print("Gasolina premium.")
    print(f"Precio por litro: ${premium:.2f}")
    litros = float(input("Ingresa la cantidad de litros: "))
    total = litros * premium
    print(f"Total de litros: {litros}L, total a pagar: ${total:.2f}")