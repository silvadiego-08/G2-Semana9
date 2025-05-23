matriz = [[2.6, 4.8], [3.9, 4.4], [5.1, 6.2], [7.3, 8.4]]
print("-" * 17)
for fila in matriz:
    for columna in fila:
        print(f"{columna:>6}", end = " ")
    print("|")
    print("-" * 17)