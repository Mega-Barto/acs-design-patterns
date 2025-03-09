from abc import ABC, abstractmethod

class AlgorithmOptimization(ABC):
    @abstractmethod
    def update(self, state):
        pass
