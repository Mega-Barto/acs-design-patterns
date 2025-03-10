from abc import ABC, abstractmethod
from model.cuenta import Cuenta

class ICuenta(ABC):
    @abstractmethod
    def retirar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        pass

    @abstractmethod
    def depositar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        pass

    @abstractmethod
    def mostrar_saldo(self, cuenta: Cuenta) -> None:
        pass
