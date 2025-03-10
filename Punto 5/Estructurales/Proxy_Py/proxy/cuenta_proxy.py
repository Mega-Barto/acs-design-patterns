import logging
from inter.icuenta import ICuenta
from inter.impl.cuenta_banco_a import CuentaBancoA
from model.cuenta import Cuenta

logging.basicConfig(level=logging.INFO)

class CuentaProxy(ICuenta):
    def __init__(self, cuenta_real: ICuenta = None):
        self.cuenta_real = cuenta_real or CuentaBancoA()

    def retirar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        logging.info("----Cuenta Proxy - Retirar Dinero----")
        return self.cuenta_real.retirar_dinero(cuenta, monto)

    def depositar_dinero(self, cuenta: Cuenta, monto: float) -> Cuenta:
        logging.info("----Cuenta Proxy - Depositar Dinero----")
        return self.cuenta_real.depositar_dinero(cuenta, monto)

    def mostrar_saldo(self, cuenta: Cuenta) -> None:
        logging.info("----Cuenta Proxy - Mostrar Dinero----")
        self.cuenta_real.mostrar_saldo(cuenta)
