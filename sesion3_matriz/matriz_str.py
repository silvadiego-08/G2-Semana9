matriz = [["Andres", "Leticia" , "Jonathan" ], ["Billy", "Goofy", "Betty"], ["Chilote", "Claudia", "Steven"]]

print("-" * 47)
for fila in matriz:
    print("|", end = " ")
    for columna in fila:
        print(f"{columna:>14}", end = " ")
    print("|")
    print("-" * 47)