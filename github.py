while True:
    for i in range(10):
        print(i)
    opcion=input("Desea volver a imprimir? (si/no)")
    if opcion == "si":
        continue
    elif opcion == "no":
        break