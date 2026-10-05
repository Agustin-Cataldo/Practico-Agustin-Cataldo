def Mostrar_menu(opciones):
    for i in range(len(opciones)):
        print(i + 1, "-", opciones[i])
    numero = int(input("Elija una opción: "))
    return opciones[numero - 1]


def buscar(lista, valor_buscado):
    for i in range(len(lista)):
        inicio= i
        fin = len(lista) - 1 - i
        if inicio > fin:
            break
        if lista[inicio] == valor_buscado:
            return True
        if lista[fin] == valor_buscado:
            return True
    return False