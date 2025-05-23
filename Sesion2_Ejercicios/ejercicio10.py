import random

lista = [random.randint(1, 100) for i in range(20)] # random.randint(1, 100) genera un número aleatorio entre 1 y 100 y for repite este proceso 20 veces

# Sumar los elementos que esten en una posicion par en la lista
suma = 0
for i in range(len(lista)):
    if i % 2 == 0: # i % 2 == 0 verifica si la posicion es par
        suma += lista[i]
print("Lista original:", lista)
print("Suma de los elementos en posiciones pares:", suma)