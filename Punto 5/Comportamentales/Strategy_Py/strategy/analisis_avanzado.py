from abc import ABC, abstractmethod
from strategy.i_estrategia import IEstrategia

class AnalisisAvanzado(IEstrategia, ABC):
    def analizar(self):
        self.iniciar()
        self.analizar_memoria()
        self.analizar_keyloggers()
        self.analizar_rootkits()
        self.descomprimir_zip()
        self.detener()

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def analizar_memoria(self):
        pass

    @abstractmethod
    def analizar_keyloggers(self):
        pass

    @abstractmethod
    def analizar_rootkits(self):
        pass

    @abstractmethod
    def descomprimir_zip(self):
        pass

    @abstractmethod
    def detener(self):
        pass
