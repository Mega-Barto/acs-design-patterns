from abc import ABC, abstractmethod

# src/inter/IConexion.py
class IConexion(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass