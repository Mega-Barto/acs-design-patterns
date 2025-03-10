class Cuenta:
    def __init__(self, id_cuenta: int, usuario: str, saldo_inicial: float):
        self.id_cuenta = id_cuenta
        self.usuario = usuario
        self.saldo_inicial = saldo_inicial

    def __str__(self):
        return f"Cuenta {self.id_cuenta} - Usuario: {self.usuario}, Saldo: {self.saldo_inicial}"
