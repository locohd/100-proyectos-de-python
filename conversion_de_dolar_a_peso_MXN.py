opcion = ""
while opcion != "3":
    print("\n Bienvenido al conversor de dólares a pesos mexicanos (MXN)")
    print("1. Convertir dólares a pesos mexicanos")
    print("2. convertir pesos mexicanos a dolares")
    print("3. Salir")
    opcion = input("Eligar una opcion: ")
    if opcion == "1":
        dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
        pesos = dolares * 16.94
        print(f"{dolares:.2f} dólares equivale a {pesos:.3f} pesos mexicanos.")
    elif opcion == "2":
        pesos = float(input("Ingrese la cantidad de pesos mexicano a convertir: "))
        dolares = pesos / 16.94
        print(f"{pesos:.2f} pesos mexicano equivale a {dolares:.3f} dólares.")
    elif opcion == "3":
        print("Gracias por usar el conversor de dólares a pesos mexicanos. ¡Hasta luego!.")
    else:
        print("Opción no válidar. Por favor ingresa una opción válida.")
    