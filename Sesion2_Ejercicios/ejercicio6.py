numeros_usuario = []

for numero in range(11):
    num = int(input("Ingrese un número entero: "))
    if num < 0:
        print("El número no puede ser negativo. Intente nuevamente.")
        continue  # Volver a pedir el número
    elif num == 0:
        print("El número es cero")
    else:
        numeros_usuario.append(num)
# Imprimir la lista de números ingresados inversamente
print("Lista de números ingresados (inversa):", numeros_usuario[::-1])