from inter.Iconexion import IConexion

class ConexionSQLServer(IConexion):
    def __init__(self):
        self.host = "localhost"
        self.puerto = "1433"
        self.usuario = "postgres"
        self.contrasena = "123"

    def conectar(self):
        print("Se conectó a SQLServer")

    def desconectar(self):
        print("Se desconectó de SQLServer")