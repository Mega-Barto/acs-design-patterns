from abc import ABC, abstractmethod
from strategy.i_estrategia import IEstrategia

class AnalisisSimple(IEstrategia, ABC):
    def analizar(self):
        self.iniciar()
        self.saltar_zip()
        self.detener()

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def saltar_zip(self):
        pass

    @abstractmethod
    def detener(self):
        pass
