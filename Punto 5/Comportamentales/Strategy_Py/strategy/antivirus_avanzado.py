import time
from strategy.analisis_avanzado import AnalisisAvanzado

class AntivirusAvanzado(AnalisisAvanzado):
    def iniciar(self):
        print("Antivirus Avanzado - Análisis avanzado iniciado")

    def analizar_memoria(self):
        try:
            print("Analizando Memoria RAM...")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

    def analizar_keyloggers(self):
        try:
            print("Analizando en busca de Keyloggers...")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

    def analizar_rootkits(self):
        try:
            print("Analizando en busca de RootKits...")
            time.sleep(1.5)
        except Exception as e:
            print(f"Error: {e}")

    def descomprimir_zip(self):
        try:
            print("Analizando archivos zip...")
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")

    def detener(self):
        print("Antivirus Avanzado - Análisis avanzado finalizado")
