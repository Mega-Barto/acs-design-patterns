# Clase que maneja la estrategia seleccionada
from models.strategy import SortStrategy


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, lista, ascendente=True):
        return self.strategy.sort(lista, ascendente)
