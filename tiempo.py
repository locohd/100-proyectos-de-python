#ese programa calcula el tiempo de un evento a que hora se va terminar
hour = int(input("Ingrese la hora de inicio del evento (0-24): "))
minute = int(input("Ingrese los minutos de inicio del evento (0-59): "))
duration = int(input("Ingrese la duración del evento en minutos: "))
total_m = (hour * 60) + minute + duration
minutofinal = total_m % 60 
total_h = total_m // 60
horafinal = total_h % 24
print(f"El evento terminará a las {horafinal}:{minutofinal}")