# proyecto 9: Tabla de multiplicar
print("=== TABLA DE MULTIPLICAR ===")
numero = int(input("Ingresa un número para ver la tabla de multplicar: "))
print(f"\n--- TABLA DEL {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")