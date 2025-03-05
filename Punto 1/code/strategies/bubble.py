from models.strategy import SortStrategy


class Bubble(SortStrategy):
    def sort(self, lista, ascendent=True):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if (ascendent and lista[j] > lista[j+1]) or (not ascendent and lista[j] < lista[j+1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista