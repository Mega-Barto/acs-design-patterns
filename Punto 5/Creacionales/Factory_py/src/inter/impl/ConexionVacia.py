from inter.Iconexion import IConexion

class ConexionVacia(IConexion):
    def conectar(self):
        print("NO SE ESPECIFICÓ PROVEEDOR")

    def desconectar(self):
        print("NO SE ESPECIFICÓ PROVEEDOR")