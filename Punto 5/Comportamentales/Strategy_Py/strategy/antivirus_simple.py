import time
from strategy.analisis_simple import AnalisisSimple

class AntivirusSimple(AnalisisSimple):
    def iniciar(self):
        print("Antivirus Simple - Análisis simple iniciado")

    def saltar_zip(self):
        try:
            print("Analizando...")
            time.sleep(2.5)
            print("No se pudo analizar archivos con extensión '.zip'")
        except Exception as e:
            print(f"Error: {e}")

    def detener(self):
        print("Antivirus Simple - Análisis simple finalizado")
