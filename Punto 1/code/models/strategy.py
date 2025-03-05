from abc import ABC, abstractmethod

# Interfaz para los algoritmos de ordenación
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, lista, ascendent=True):
        pass
