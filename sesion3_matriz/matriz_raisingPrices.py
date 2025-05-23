precios_originales = [[55, 60, 65],
                        [70, 75, 80],
                        [85, 90, 95]]

for fila in precios_originales:
    for columna in fila:
        print(f"{columna:>6}", end = " ")
    print("|")
    print("-" * 17)
    
# Aumentar los precios en un 15%
precios_aumentados = [[columna * 1.15 for columna in fila] for fila in precios_originales]
print("-" * 17)
for fila in precios_aumentados:
    for columna in fila:
        print(f"{columna:>6.2f}", end = " ")
    print("|")
    print("-" * 17)
