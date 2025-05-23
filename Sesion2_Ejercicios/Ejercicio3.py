calificacion = []

for i in range(1, 9):
    if nota < 0:
        print("La calificación no puede ser negativa. Intente nuevamente.")
        continue  # Volver a pedir la calificación
    nota = int(input(f"Ingrese la calificación {i} del estudiante: "))
    calificacion.append(nota)  # Agregar la calificación a la lista

# Calcular el promedio
promedio = sum(calificacion) / len(calificacion)
print("La calificación promedio es:", promedio)
