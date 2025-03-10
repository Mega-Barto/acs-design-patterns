from inter.icuenta import ICuenta
from model.cuenta import Cuenta

class CuentaBancoB(ICuenta):
    def retirar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        cuenta.saldo_inicial -= monto
        print(f"Saldo actual: {cuenta.saldo_inicial}")
        return cuenta

    def depositar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        cuenta.saldo_inicial += monto + 0.20  # Agrega una bonificación de 0.20
        print(f"Saldo actual: {cuenta.saldo_inicial}")
        return cuenta

    def mostrar_saldo(self, cuenta: Cuenta) -> None:
        print(f"Saldo actual: {cuenta.saldo_inicial}")
