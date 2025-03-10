from inter.Iconexion import IConexion

class ConexionMySQL(IConexion):
    def __init__(self):
        self.host = "localhost"
        self.puerto = "3306"
        self.usuario = "root"
        self.contrasena = "123"

    def conectar(self):
        print("Se conectó a MySQL")

    def desconectar(self):
        print("Se desconectó de MySQL")
