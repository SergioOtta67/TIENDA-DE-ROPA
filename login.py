import csv
import getpass
from librerias import menu

def busqueda(ruta : str, usuario : str, password : str) -> int:
    global ventas, agregar
    with open(ruta, newline="", encoding="utf-8") as archivo:
        ### DictReader: Salida Diccionario
        ### reader    : Salida formato lista
        info = csv.DictReader(archivo)
        sale = 0
        for fila in info:
            if fila.get("Usuario")==usuario: 
                if fila.get("Ventas")=="S":
                    ventas = 1
                else:
                    ventas = 0
                if fila.get("Agregar")=="S":
                    agregar = 1
                else:
                    agregar = 0
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
    #passw = getpass(input("Ingrese Password : "))
    try:
        password = getpass.getpass("Ingrese Password : ")
    except Exception as err:
        print('ERROR:', err)
    global ventas, agregar
    ventas  = 0
    agregar = 0
    vale    = busqueda("usuarios.csv", usuario, password)
    if vale==1:
        print ("\n"*8)
        print(f"Bienvenido {usuario}\n")
        if bool(ventas) and bool(agregar):
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas", "Agregar Articulos\n", "Salir\n"]
            #opc = menu("Tienda de Ropa y Accesorios", lista, 5, 1, usuario)
        elif bool(ventas) and (not bool(agregar)):
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas\n", "Salir\n"]
            #opc = menu("Tienda de Ropa y Accesorios", lista, 4, 1, usuario)
        else:
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock\n", "Salir\n"]
        opc = menu("Tienda de Ropa y Accesorios", lista, len(lista), 1, usuario)
            
        print (f"\n\nTu Opcion : {opc}\n")
    elif vale==2:
        print("La Passord Ingresada es Incorrecta ")
    elif vale==3:
        print("El Usuario Ingresado No se Ecuentra ")
    else:
        print("Usuario y Password Ingresadas son Incorrectas\n\n")
    