saldo = 1000
while True:
    print("\n---Cajero Automático---")
    print("1.- Consultar saldo")
    print("2.- Retirar efectivo")
    print("3.- Depositar efectivo")
    print("4.- Salir")
    opcion = input("Seleccione una opción: ")
    #Las opciones del menú 
    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
        input("Presione Enter para continuar...")
    elif opcion == "2":
        monto_retirar = float(input("Ingrese el monto a retirar: "))
        if monto_retirar <= saldo:
            saldo -= monto_retirar
            print(f"Ha retirado ${monto_retirar}. Su nuevo saldo es: ${saldo}")
            input("Presione Enter para continuar...")
        else:
            print("Saldo insuficiente para realizar el rettiro.")
    elif opcion == "3":
        monto_depositar = float(input("Ingrese el monto a depositar: "))
        saldo += monto_depositar
        print(f"Ha depositado ${monto_depositar}. Su nuevo saldo es: ${saldo}")
        input("Presione Enter para continuar...")
    elif opcion == "4":
        print("Gracias por usar el cajero automático. !Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")