import os
from container.archivo import Archivo
class ContadorDePalabras:
    def __init__(self, carpeta):
        self.carpeta = carpeta

    def contar_palabras_en_carpeta(self, palabra_buscada):
        if not os.path.exists(self.carpeta):
            print("¡La carpeta indicada no existe!")
            return

        archivos_texto = self._buscar_archivos()
        if not archivos_texto:
            print("No se encontraron archivos de texto en la carpeta.")
            return

        total_palabras = 0
        for archivo in archivos_texto:
            archivo_obj = Archivo(archivo)
            cantidad_palabras = archivo_obj.contar_palabras(palabra_buscada)
            print(f"{archivo}: {cantidad_palabras} veces")
            total_palabras += cantidad_palabras

        print(f"Total: {total_palabras} veces")

    def _buscar_archivos(self):
        archivos_texto = []
        for archivo in os.listdir(self.carpeta):
            if archivo.endswith(('.txt', '.xml', '.json', '.csv')):
                archivos_texto.append(os.path.join(self.carpeta, archivo))
        return archivos_texto