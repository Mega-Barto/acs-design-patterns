from abc import ABC, abstractmethod

class IEstrategia(ABC):
    @abstractmethod
    def analizar(self):
        pass
