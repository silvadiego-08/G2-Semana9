lista = ["perro", "gato", "pez", "ave", "caballo", "tortuga", "conejo", "hámster", "iguana", "serpiente"]

while True:
    palabra = input("Ingrese un animal: ")
    if palabra in lista:
        print("El animal está en la lista")
        break
    else:
        print("El animal no está en la lista")