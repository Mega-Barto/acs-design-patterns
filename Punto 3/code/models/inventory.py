from typing import List
from models.algorithm import AlgorithmOptimization

class Inventory:
    def __init__(self):
        self._observers: List[AlgorithmOptimization] = []
        self._state = {}

    def add_observer(self, observer: AlgorithmOptimization):
        self._observers.append(observer)

    def remove_observer(self, observer: AlgorithmOptimization):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def update_state(self, state: dict):
        self._state = state
        self.notify_observers()
