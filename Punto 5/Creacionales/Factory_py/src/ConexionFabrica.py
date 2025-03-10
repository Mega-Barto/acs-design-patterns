from inter.impl.ConexionMySQL import ConexionMySQL
from inter.impl.ConexionOracle import ConexionOracle
from inter.impl.ConexionPostgresSQL import ConexionPostgreSQL
from inter.impl.ConexionSQLServer import ConexionSQLServer
from inter.impl.ConexionVacia import ConexionVacia

class ConexionFabrica:
    @staticmethod
    def get_conexion(motor):
        if motor is None:
            return ConexionVacia()
        motores = {
            "MYSQL": ConexionMySQL,
            "ORACLE": ConexionOracle,
            "POSTGRE": ConexionPostgreSQL,
            "SQL": ConexionSQLServer
        }
        return motores.get(motor.upper(), ConexionVacia)()
