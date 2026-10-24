# Ese progrma calcula el costo total de un servicio incluyendo la propina.
costo = int(input("Ingrese el costo del servicio: "))
propina = int(input("Ingrese el porcentaje de propina que desea dejar: "))

total_propina = costo * (propina / 100) # aqui hace la operacion para calcular la propina.
total = costo + total_propina # aqui suma el costo del servicio con la propina para obtener el total.
print(f"El costo total del servicio incluyendo la propina es: {total} ") # Imprime el ressultado final al usuario.