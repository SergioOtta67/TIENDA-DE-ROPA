from producto import Producto

class Ropa(Producto):
    def __init__ (self,
                codigo : str, 
                talle  : str,
                genero : str,
                precio : float | None = 0, 
                stock : int | None = 0, 
                descripcion : str | None = "") -> None:
        super().__init__(codigo, precio, stock, descripcion)
        self.__talle = talle
        self.__genero = genero
        self.lista_talles = ["XS", "S", "M", "L", "XL", "XXL"]
        self.lista_generos = ["Masculino", "Femenino", "Unisex"]

    def get_talle(self) -> str:
        return self.__talle

    def get_genero(self) -> str:
        return self.__genero

