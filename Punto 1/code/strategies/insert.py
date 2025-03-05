from models.strategy import SortStrategy


class Insert(SortStrategy):
    def sort(self, lista, ascendent=True):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and ((ascendent and lista[j] > key) or (not ascendent and lista[j] < key)):
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return lista