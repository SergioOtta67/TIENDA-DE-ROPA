import csv
from productos import *


class Importador():
    @classmethod
    def importar(cls, ruta : str):
        with open(ruta, newline="", encoding="utf-8") as archivo:
            ### DictReader: Salida Diccionario
            ### reader    : Salida formato lista
            info = csv.DictReader(archivo)
            for fila in info:
                print(fila)  # O realiza alguna operación con cada fila
        #with open(ruta, newline="", encoding="utf-8") as archivo:
        #    info = csv.reader(archivo)
        #    for fila in info:
        #        print(fila)  # O realiza alguna operación con cada fila


if __name__ == "__main__":
    #Importador.importar("ropa.csv")
    Importador.importar("accesorios.csv")