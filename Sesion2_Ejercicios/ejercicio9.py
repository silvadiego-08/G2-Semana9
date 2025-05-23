import random

lista = [random.randint(1, 100) for _ in range(11)] # random.randint(1, 100) genera un número aleatorio entre 1 y 100 y for repite este proceso 10 veces

lista_con_numeros_pares = [num for num in lista if num % 2 == 0] # num % 2 == 0 verifica si el número es par
lista_con_numeros_impares = [num for num in lista if num % 2 != 0] # num % 2 != 0 verifica si el número es impar
print("Lista original:", lista)
print("Lista de números pares:", lista_con_numeros_pares)
print("Lista de números impares:", lista_con_numeros_impares)