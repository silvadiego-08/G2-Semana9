lista_con_repetidos = []

while True:
    numero = int(input("Ingrese un número (o 0 para terminar): "))
    if numero == 0:
        print("Número cero ingresado. Terminando el programa.") # Bucle el cual termina cuando el usuario desee.
        break
    else:
        lista_con_repetidos.append(numero)

# Eliminar duplicados
lista_sin_repetidos = list(set(lista_con_repetidos))
# Ordenar la lista
lista_sin_repetidos.sort()
# Imprimir la lista sin duplicados
print("Lista sin duplicados y ordenada:", lista_sin_repetidos)
# Imprimir la lista original
print("\nLista original con duplicados:", lista_con_repetidos)