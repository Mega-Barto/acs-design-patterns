from ConexionFabrica import ConexionFabrica

if __name__ == "__main__":
    fabrica = ConexionFabrica()

    cx1 = fabrica.get_conexion("ORACLE")
    cx1.conectar()
    cx1.desconectar()

    cx2 = fabrica.get_conexion("MYSQL")
    cx2.conectar()
    cx2.desconectar()

    cx3 = fabrica.get_conexion("H2")
    cx3.conectar()
    cx3.desconectar()
