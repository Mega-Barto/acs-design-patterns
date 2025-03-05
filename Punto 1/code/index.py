from strategies.bubble import Bubble
from strategies.insert import Insert
from strategies.quick import QuickSort
from context.sorter import Sorter


if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    
    strategies = {"burbuja": Bubble(), "quicksort": QuickSort(), "insercion": Insert()}

    while True:
        algorithm = input("Seleccione algoritmo (burbuja, quicksort, insercion): ").lower()
        if algorithm in strategies:
            break
        print("Algoritmo no válido. Intente nuevamente.")

    while True:
        order = input("Orden (asc/desc): ").lower()
        if order in ["asc", "desc"]:
            order = order == "asc"
            break
        print("Entrada inválida. Debe ser 'asc' o 'desc'.")

    sorter = Sorter(strategies[algorithm])
    print("Lista ordenada:", sorter.sort(lista, order))

