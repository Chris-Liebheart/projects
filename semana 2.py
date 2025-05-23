# Paso 1: Pedimos una calificacion y verificamos si aprobo
calificacion = int(input("Ingresa tu calificacion (0-100): "))

if calificacion >= 60:
    print("Has aprobado! ")
else:
    print("Has reprobado, sigue esforzandote. ")

# Paso 2: Pedimos una lista de calificaciones y calculamos el promedio
calificaciones_str = input("Ingresa una lista de calificaciones separadas por comas: ")
calificaciones = [int(c) for c in calificaciones_str.split(",")]  # Convertimos las calificaciones a numeros

promedio = int (sum(calificaciones) / len(calificaciones))
print(f"El promedio de tus calificaciones es: {promedio}")

# Paso 3: Contamos cuantas calificaciones son mayores a un numero dado

valor = int(input("Ingresa un valor para comparar: "))
contador_mayores = sum(1 for c in calificaciones if c > valor)
print(f"Hay {contador_mayores} calificaciones mayores que {valor}.")

# Paso 4: Buscamos una calificacion especifica y contamos cuantas veces aparece
calificacion_especifica = int(input("Ingresa una calificacion para buscar: "))
contador = 0

for c in calificaciones:
    if c == calificacion_especifica:
        contador =contador + 1
    elif c > calificacion_especifica:  # 'continue'
        continue
    elif c < calificacion_especifica:  #  'break'
        break

print(f"La calificacion {calificacion_especifica} aparece {contador} veces.")
