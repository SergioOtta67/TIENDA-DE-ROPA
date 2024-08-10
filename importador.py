import csv
from productos.ropa import Ropa
from productos.accesorio import Accesorio
#from .productos.producto import Producto
class Importador():
    @classmethod
    def importar(cls, ruta : str):
        with open(ruta, newline="", encoding="utf-8") as archivo:
            ### DictReader: Salida Diccionario
            ### reader    : Salida formato lista
            info = csv.DictReader(archivo)
            lista = []
            for linea in info:
                codigo = linea.get("Codigo")
                precio = linea.get("Precio")
                stock  = linea.get("Stock")
                descripcion = linea.get("Descripcion")
                if "Talle" in linea.keys():
                    talle  = linea.get("Talle")
                    genero = linea.get("Genero")
                    lista.append(Ropa(codigo, talle, genero, precio, stock, descripcion))
                elif "Material" in linea.keys():
                    material = linea.get("Material")
                    lista.append(Accesorio(codigo, material, precio, stock, descripcion))
        return lista


if __name__ == "__main__":
    articulos = []
    articulos = Importador.importar("./csv/ropa.csv")
    articulos.extend(Importador.importar("./csv/accesorios.csv"))
    for arti in articulos:
        print(arti.get_info())