import random
numero_secreto = random.randint(1, 100)
intentos = 0
print("----ADIVINA EL NUMERO---")
print("EStoy pensando en un número del 1-100")
#Aqui es donde le pedimos al usuario ingrese un número
while True:
    mi_numero = int(input("Ingrsa tu Número del 1-100"))
    intentos += 1
    if mi_numero < numero_secreto:
        print("El número secreto es mayor")
    elif mi_numero > numero_secreto:
        print("El número es menor")
    else:
        print("Adivinastes el numero")
        print("intentos", intentos)
        break