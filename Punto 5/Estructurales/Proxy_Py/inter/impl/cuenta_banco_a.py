from inter.icuenta import ICuenta
from model.cuenta import Cuenta

class CuentaBancoA(ICuenta):
    def retirar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        cuenta.saldo_inicial -= monto
        print(f"Saldo actual: {cuenta.saldo_inicial}")
        return cuenta

    def depositar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        cuenta.saldo_inicial += monto
        print(f"Saldo actual: {cuenta.saldo_inicial}")
        return cuenta

    def mostrar_saldo(self, cuenta: Cuenta) -> None:
        print(f"Saldo actual: {cuenta.saldo_inicial}")
