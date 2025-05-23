numeros_reales = []

while True:
    numero = float(input("Ingrese un número real (o numero negativo para terminar): "))
    if numero == 0:
        print("Número negativo ingresado. Terminando el programa.")
        break
    else:
        numeros_reales.append(numero)
 
# Encontrar el numero mayor y menor
mayor = max(numeros_reales)
menor = min(numeros_reales)
print("El número mayor es:", mayor)
print("El número menor es:", menor)