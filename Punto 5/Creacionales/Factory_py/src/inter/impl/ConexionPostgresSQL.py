from inter.Iconexion import IConexion

class ConexionPostgreSQL(IConexion):
    def __init__(self):
        self.host = "localhost"
        self.puerto = "5433"
        self.usuario = "postgres"
        self.contrasena = "123"

    def conectar(self):
        print("Se conectó a PostgreSQL")

    def desconectar(self):
        print("Se desconectó de PostgreSQL")