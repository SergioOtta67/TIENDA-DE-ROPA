import csv
from productos.ropa import Ropa
from productos.accesorio import Accesorio
#from .productos.producto import Producto
class Importador():
    @classmethod
    def importar(cls, ruta : str) -> list[object]:
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
    
    @classmethod
    def exportar(cls, 
                 nombre   : str, 
                 stock    : int, 
                 precio   : float, 
                 genero   : str | None = "", 
                 talle    : str | None = "", 
                 material : str | None = ""):
        if material=="":
            ruta = "./csv/ropa.csv"
        else:
            ruta = "./csv/accesorios.csv"
        articulo = {}   
        with open (ruta, mode="a", encoding="utf-8") as archivo:
            titulo = ["Codigo","Precio","Stock","Descripcion"]
            if material=="":
                titulo.insert(1, "Genero")
                titulo.insert(1, "Talle")
            else:
                titulo.insert(1, "Material")
            escribir = csv.DictWriter(archivo, titulo)
            escribir.writerow(articulo)
        return 


if __name__ == "__main__":
    articulos = []
    articulos = Importador.importar("./csv/ropa.csv")
    articulos.extend(Importador.importar("./csv/accesorios.csv"))
    for arti in articulos:
        print(arti.get_info())