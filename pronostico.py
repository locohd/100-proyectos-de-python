#Este programa calcula el tiempo de hoy te dice una recomendación del clima.
c = float(input("Ingresa la temperatura actual en grados Celsius: "))
f = (c * 1.8) + 32 # Convierte la temperatura de Celsius a Fahrenheit.
print(f"\n{c}°C equivalen a {f:.1f}°F.")
print("Recomendación del clima: ")
if f < 68:
    print("Hace mucho frío, abrígate bien.")
elif f < 85:
    print("El clima es agradable.")
elif f <= 90:
    print("Hace mucho calor, hidrátate y evita la exposición al sol.")
else:
    print("¡Hace un calor extremo! Ten mucho cuidado.")
