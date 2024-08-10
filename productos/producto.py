class Producto():
    def __init__ (self,
                codigo:str, 
                precio : float | None = 0, 
                stock : int | None = 0, 
                descripcion : str | None = "" ) -> None:
        self.__codigo = codigo
        self.__precio = precio
        self.__stock = stock
        self.__descripcion = descripcion

    def agregar_stock(self, numero : int):
        self.__stock += numero
    
    def set_stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    def get_codigo(self) -> str:
        return self.__codigo

    def get_precio(self) -> float:
        return self.__precio

    def get_stock(self) -> int:
        return self.__stock

    def get_descripcion(self) -> str:
        return self.__descripcion
    
    def get_info(self):
        return {
                "Codigo"      : self.__codigo,
                "Precio"      : self.__precio,
                "Stock"       : self.__stock,
                "Descripcion" : self.__descripcion
                }