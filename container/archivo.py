import re

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def contar_palabras(self, palabra_buscada):
        try:
            with open(self.nombre, 'r', encoding='utf-8') as file:
                contenido = file.read()
                count = len(re.findall(r'\b{}\b'.format(re.escape(palabra_buscada.lower())), contenido.lower()))
                return count
        except Exception as e:
            print(f"Error al leer el archivo {self.nombre}: {e}")
            return 0