from models.strategy import SortStrategy


class QuickSort(SortStrategy):
    def sort(self, lista, ascendent=True):
        if len(lista) <= 1:
            return lista
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot] if ascendent else [x for x in lista if x > pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot] if ascendent else [x for x in lista if x < pivot]
        return self.sort(left, ascendent) + middle + self.sort(right, ascendent)