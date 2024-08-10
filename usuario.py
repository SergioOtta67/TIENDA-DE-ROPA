class Usuario():
    def __init__(self, nombre, password, venta, agregar) -> None:
        self.__nombre   = nombre
        self.__password = password
        self.__venta    = venta
        self.__agregar  = agregar
    
    def inicio_session(self, nombre, password):
        return nombre == self.__nombre and password == self.__password
