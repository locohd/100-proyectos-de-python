# Ese programa calcula el costo total de un servicio incluyendo la propina.
costo = float(input("Ingrese el costo del servicio: "))
propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

total_propina = costo * (propina / 100) # aqui hace la operacion para calcular la propina.
total = costo + total_propina # aqui suma el costo del servicio con la propina para obtener el total.

if costo < 0 or propina < 0:
    print("Error: El costo del servicio y el porcentaje de propina deben ser números positivos.") # Imprime un mensaje de error si el costo o la propina son negativos.
else:
    print(f"El costo total del servicio incluyendo la propina es: {total:.2f} ") # Imprime el resultado final al usuario.
