import os
import random

participantes = list()
while True:
    os.system("cls")
    os.system("color 0c")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    print("Participante ingresado con exito")  # Mensaje de confirmación
    input("Presione Enter para continuar...")  # Pausa para ver el mensaje


os.system("cls")
print(participantes)

fin = len(participantes)
ganador = random.randint(0, fin - 1)
print("El ganador es:", participantes[ganador])
