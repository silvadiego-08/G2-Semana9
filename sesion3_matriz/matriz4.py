matriz = [["Andres", "Leticia", "Jonathan"], 
          ["Billy", "Goofy", "Betty"], 
          ["Chilote", "Claudia", "Steven"]]

for fila in matriz: # Imprimir la matriz
    for columna in fila:
        print(f"{columna:>6}", end = " ")
    print("|")
    print("-" * 21)

# Imprimir otra matriz con la cantidad de letras que tiene cada nombre
matriz2 = [[len(columna) for columna in fila] for fila in matriz]
print("-" * 21)
for fila in matriz2: # Imprimir la matriz
    for columna in fila:
        print(f"{columna:>6}", end = " ")
    print("|")
    print("-" * 21)


