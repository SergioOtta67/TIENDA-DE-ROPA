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
    global ventas, agregar, cambiar_permisos, modificar_stock
    with open(ruta, newline="", encoding="utf-8") as archivo:
        ### DictReader: Salida Diccionario
        ### reader    : Salida formato lista
        info = csv.DictReader(archivo)
        sale = 3
        for fila in info:
            if fila.get("Usuario")==usuario: 
                ventas  = bool(fila.get("Ventas"))
                agregar = bool(fila.get("Agregar"))
                cambiar_permisos = bool(fila.get("CambiarPermisos"))
                modificar_stock  = bool(fila.get("ModificarStock"))
                if fila.get("Password")==password:
                    sale = 1
                    break
                else:
                    sale = 2
                    break
        return sale

def formatear_precio(precio : float | None = 0) -> str:
    precio_info  = f"{precio:,.2f}"
    precio_info  = precio_info.replace(",", "X").replace(".", ",").replace("X", ".")
    precio_info  = "***************" + precio_info
    return precio_info

if __name__ == "__main__":
    print("####  L O G I N  ####")
    usuario = input("Ingrese Usuario  : ")
    try:
        password = getpass.getpass("Ingrese Password : ")
    except Exception as err:
        print('ERROR:', err)
    global ventas, agregar, cambiar_permisos, modificar_stock
    ventas  = False
    agregar = False
    cambiar_permisos = False
    modificar_stock  = False
    vale    = busqueda("./csv/usuarios.csv", usuario, password)
    if vale==1:
        print ("\n"*8)
        print(f"Bienvenido {usuario}\n")
        if ventas and agregar:
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock\n", "Realizar Ventas\n", "Agregar Articulos", "Modificar Articulos\n", "Cambiar Permisos\n", "Salir\n"]
        elif ventas and (not agregar):
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "\nRealizar Ventas\n", "Salir\n"]
        else:
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock\n", "Salir\n"]
        
        while True:
            opc = menu("Tienda de Ropa y Accesorios", lista, len(lista), 1, usuario)
            if opc==len(lista):
                break
            elif opc==1:
                print("\n")
                articulos = Importador.importar("./csv/ropa.csv")
                print ("Codigo|Talle|     Genero    |  Stock  |      Precio    |  Descripcion  ")
                for arti in articulos:
                    stock_int  = int(arti.get_stock())
                    if stock_int > 0:
                        stock        = arti.get_stock()
                        codigo       = arti.get_codigo()
                        descripcion  = arti.get_descripcion()
                        precio_info  = formatear_precio(float(arti.get_precio()))
                        espacio      = " "*4
                        talle        = arti.get_talle()
                        genero       = arti.get_genero()
                        #print(arti.ropa.get_info_renglon())
                        print(f"{codigo:6}| {talle:4}|     {genero:10}|   {('****' + str(stock))[-4:]}  | {precio_info[-15:]}|  {descripcion}")
                print("\n")
                
            elif opc==2:
                print("\n")
                articulos = Importador.importar("./csv/accesorios.csv")
                print ("Codigo|      Material      |  Stock  |      Precio      |  Descripcion  ")
                for arti in articulos:
                    stock_int  = int(arti.get_stock())
                    if stock_int > 0:
                        stock        = arti.get_stock()
                        codigo       = arti.get_codigo()
                        descripcion  = arti.get_descripcion()
                        precio_info  = formatear_precio(float(arti.get_precio()))
                        espacio      = " "*3
                        material     = arti.get_material()
                        print(f" {codigo:4} |  {material:18}|{espacio}{('****' + str(stock))[-4:]}  |  {precio_info[-15:]} | {descripcion}")
                print("\n")

            elif opc==3 and ventas:
                pass
            elif opc==4 and agregar:
                #articulos         = Importador.importar("./csv/ropa.csv")
                #codigo_de_ropa    = articulos[-1].get_info().get("Codigo")
                #print(f"Ultimo codigo Ropa = {codigo_de_ropa}")
                #articulos         = Importador.importar("./csv/accesorios.csv")
                #codigo_accesorios = articulos[-1].get_info().get("Codigo")
                #print(f"Ultimo codigo accesorios = {codigo_accesorios}")
                
                #
                # Puesto en 2 renglones
                # se posiciona en el ultimo componente
                # extraigo la informacion con el metodo correspondiente
                # y luego hago un get("Codigo") para extraer el valor en cuestion
                #
                codigo_de_ropa    = Importador.importar("./csv/ropa.csv")[-1].get_info().get("Codigo")
                print(f"\nUltimo codigo de Ropa    = {codigo_de_ropa}")
                codigo_accesorios = Importador.importar("./csv/accesorios.csv")[-1].get_info().get("Codigo")
                print(f"Ultimo Codigo Accesorios = {codigo_accesorios}")
                if codigo_de_ropa > codigo_accesorios:
                    sigue = int(codigo_de_ropa) + 1
                else:
                    sigue = int(codigo_accesorios) + 1
                print (f"Siguiente a Incorporar   = {sigue}\n")

            else:
                print("La opcion es incorrecta")
    elif vale==2:
        print("La Passord Ingresada es Incorrecta ")
    elif vale==3:
        print("El Usuario Ingresado No se Ecuentra ")
    else:
        print("Usuario y Password Ingresadas son Incorrectas\n\n")
    