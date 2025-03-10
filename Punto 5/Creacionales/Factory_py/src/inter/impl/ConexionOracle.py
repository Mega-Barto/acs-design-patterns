from inter.Iconexion import IConexion

class ConexionOracle(IConexion):
    def __init__(self):
        self.host = "localhost"
        self.puerto = "1521"
        self.usuario = "admin"
        self.contrasena = "123"

    def conectar(self):
        print("Se conectó a Oracle")

    def desconectar(self):
        print("Se desconectó de Oracle")
