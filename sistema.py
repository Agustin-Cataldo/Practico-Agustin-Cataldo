from util import Mostrar_menu
from util import buscar
opciones = ["Comprar", "Devolver", "Ver precio", "Salir"]
seleccion = Mostrar_menu(opciones)
print(f"Usted seleccionó: {seleccion}")


lista =["a","b","c","d","e","f","g"]
valor_buscado = input("Cual es su valor a buscar: ")
resultado = buscar(lista, valor_buscado)
if resultado:
    print("encontrado")
elif False:
    print("inexistente")