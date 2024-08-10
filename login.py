import csv
import getpass
from librerias import menu

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
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas", "Agregar Articulos\n", "Salir\n"]
        elif ventas and (not agregar):
            lista = ["Ver Prendas c/stock", "Ver Accesorios c/stock", "Realizar Ventas\n", "Salir\n"]
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
    