from model.cuenta import Cuenta
from inter.impl.cuenta_banco_b import CuentaBancoB
from proxy.cuenta_proxy import CuentaProxy

if __name__ == "__main__":
    cuenta = Cuenta(1, "mitocode", 100)

    cuenta_proxy = CuentaProxy(CuentaBancoB())  # Se puede cambiar a CuentaBancoA
    cuenta_proxy.mostrar_saldo(cuenta)
    cuenta = cuenta_proxy.depositar_dinero(cuenta, 50)
    cuenta = cuenta_proxy.retirar_dinero(cuenta, 20)
    cuenta_proxy.mostrar_saldo(cuenta)
