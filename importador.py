import csv
from productos.ropa import Ropa

class Importador():
    @classmethod
    def importar(cls, ruta : str):
        with open(ruta, newline="") as archivo:
            info = csv.DictReader(archivo)
            

if __name__ == "__main__":
    Importador("ropa.csv")