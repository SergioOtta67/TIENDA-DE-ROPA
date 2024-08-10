import csv
import getpass
from librerias import menu
#from productos.producto import Producto
#from productos.ropa import Ropa
#from productos.accesorio import Accesorio
from importador import *

def solo_mostrar(ruta : str):
        with open(ruta, newline="", encoding="utf-8") as archivo:
            ### DictReader: Salida Diccionario
            ### reader    : Salida formato lista
            #info = csv.DictReader(archivo)
            #lista = []
            info = []
            info = Importador.importar(ruta)
            for linea in info:
                print(f"{linea}\n")
                stock  = linea.get("Stock")
                if stock > 0:
                    codigo       = linea.get("Codigo")
                    precio       = float(linea.get("Precio"))
                    descripcion  = linea.get("Descripcion")
                    precio_info  = f"{precio:,.2f}"
                    precio_info  = precio_info.replace(",", "X").replace(".", ",").replace("X", ".")
                    precio_info  = "**********" + precio_info
                    espacio = " "*5
                    if "Talle" in linea.keys():
                        talle  = linea.get("Talle")
                        genero = linea.get("Genero")
                        print(f"{codigo:5} {talle:5}{genero:15}{espacio}{('****' + stock)[-4:]}  {precio_info[-10:]}  {descripcion}")
                    elif "Material" in linea.keys():
                        material = linea.get("Material")
                        print(f"{codigo:5} {material:20}{espacio}{('****' + stock)[-4:]}  {precio_info[-10:]}  {descripcion}")

def busqueda(ruta : str, usuario : str, password : str) -> int:
    global ventas, agregar
    with open(ruta, newline="", encoding="utf-8") as archivo:
        ### DictReader: Salida Diccionario
        ### reader    : Salida formato lista
        info = csv.DictReader(archivo)
        sale = 3
        for fila in info:
            if fila.get("Usuario")==usuario: 
                ventas  = bool(fila.get("Ventas"))
                agregar = bool(fila.get("Agregar"))
                if fila.get("Password")==password:
                    sale = 1
                    break
                else:
                    sale = 2
                    break
        return sale

if __name__ == "__main__":
    print("####  L O G I N  ####")
    usuario = input("Ingrese Usuario  : ")
    try:
        password = getpass.getpass("Ingrese Password : ")
    except Exception as err:
        print('ERROR:', err)
    global ventas, agregar
    ventas  = False
    agregar = False
    vale    = busqueda("./csv/usuarios.csv", usuario, password)
    if vale==1:
        print ("\n"*8)
        print(f"Bienvenido {usuario}\n")
        if ventas and agregar:
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas", "Agregar Articulos", "Cambiar Permisos\n", "Salir\n"]
        elif ventas and (not agregar):
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas\n", "Salir\n"]
        else:
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock\n", "Salir\n"]
        
        while True:
            opc = menu("Tienda de Ropa y Accesorios", lista, len(lista), 1, usuario)
            if opc==len(lista):
                break
            elif opc==1:
                articulos = Importador.importar("./csv/ropa.csv")
                for arti in articulos:
                    stock  = int(arti.get_stock())
                    if stock > 0:
                        stock        = arti.get_stock()
                        codigo       = arti.get_codigo()
                        precio       = float(arti.get_precio())
                        descripcion  = arti.get_descripcion()
                        precio_info  = f"{precio:,.2f}"
                        precio_info  = precio_info.replace(",", "X").replace(".", ",").replace("X", ".")
                        precio_info  = "**********" + precio_info
                        espacio = " "*5
                        talle = arti.get_talle()
                        genero = arti.get_genero()
                        print(f"{codigo:5} {talle:5}{genero:15}{espacio}{('****' + str(stock))[-4:]}  {precio_info[-10:]}  {descripcion}")
            elif opc==2:
                articulos = Importador.importar("./csv/accesorios.csv")
                for arti in articulos:
                    stock  = int(arti.get_stock())
                    if stock > 0:
                        stock        = arti.get_stock()
                        codigo       = arti.get_codigo()
                        precio       = float(arti.get_precio())
                        descripcion  = arti.get_descripcion()
                        precio_info  = f"{precio:,.2f}"
                        precio_info  = precio_info.replace(",", "X").replace(".", ",").replace("X", ".")
                        precio_info  = "**********" + precio_info
                        espacio = " "*5
                        material = arti.get_material()
                        print(f"{codigo:5} {material:20}{espacio}{('****' + str(stock))[-4:]}  {precio_info[-10:]}  {descripcion}")

            elif opc==3 and ventas:
                pass
            elif opc==4 and agregar:
                pass
            else:
                print("La opcion es incorrecta")
    elif vale==2:
        print("La Passord Ingresada es Incorrecta ")
    elif vale==3:
        print("El Usuario Ingresado No se Ecuentra ")
    else:
        print("Usuario y Password Ingresadas son Incorrectas\n\n")
    