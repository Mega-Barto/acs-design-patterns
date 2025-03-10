from strategy.i_estrategia import IEstrategia

class Contexto:
    def __init__(self, estrategia: IEstrategia):
        self.estrategia = estrategia

    def ejecutar(self):
        self.estrategia.analizar()
