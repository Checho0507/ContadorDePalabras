from container.archivo import Archivo
from container.contador import ContadorDePalabras
# Prueba del programa
if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra_buscada = input("Ingrese la palabra que desea buscar: ")

    contador = ContadorDePalabras(carpeta)
    contador.contar_palabras_en_carpeta(palabra_buscada)
