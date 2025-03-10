from strategy.contexto import Contexto
from strategy.antivirus_avanzado import AntivirusAvanzado

if __name__ == "__main__":
    contexto = Contexto(AntivirusAvanzado())  # Se puede cambiar a AntivirusSimple()
    contexto.ejecutar()
