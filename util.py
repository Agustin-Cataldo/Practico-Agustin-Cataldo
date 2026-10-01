def Mostrar_menu(opciones):
    for i in range(len(opciones)):
        print(i + 1, "-", opciones[i])
    numero = int(input("Elija una opción: "))
    return opciones[numero - 1]