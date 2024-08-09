#titulo     : nombre del menú
#opciones   : lista str de las opciones que se van a imprimir
#sale       : opcion para salir del menu
#tab        : para poner tabulacion 0:no 1:si
#usuario    : nombre del usuario del menu
#return opc : es la opcion seleccionada por el usuario
#
#     SALIDA ESPERADA:::
#
#  MENU: Ingreso de Empleados ** Administrador **
#  ----------------------------------------------
#          1-Agregar
#          2-Mostrar
#          3-Mostrar Activos
#          4-Salir
#          Tu Opcion : 
def menu(titulo : str, opciones : list[str], sale : int, tab : int | None = 1, usuario : str | None = "Visitante") -> int:
    mostrar = f"MENU: {titulo} ** {usuario.capitalize()} **"
    print (f"{mostrar}")
    print ("-"*(len(mostrar)))
    tope = len(opciones)
    poner = "\t"*tab
    for x in range(tope):
        if tab>0:
            print(f"{poner}{x+1}-{opciones[x]}")
        else:
            print(f"{x+1}-{opciones[x]}")
    opc = 0
    while True:
        opc = input(f"{poner}Tu Opcion : ")
        if (opc.isdigit()): 
            opc = int(opc)
            if (opc>0 and opc<=sale):
                break
            elif (opc==0 or opc>sale):
                print("\nOpcion Incorrecta !!!!\n")
        else:
            print ("\nSeleccione solo numeros !!!!\n")
    return opc

def largo_dato(tipo_dato : int, dato_info : str) -> int:
    sale = len(dato_info)
    if tipo_dato==1 and len(dato_info)==0:
        sale = "Mi diccionario esta vacio"
    elif tipo_dato==2 and len(dato_info)==0:
        sale = "Mi lista esta vacia"
    elif tipo_dato==3 and len(dato_info)==0:
        sale = "Mi tupla esta vacia"
    elif tipo_dato==4 and len(dato_info)==0:
        sale = "Mi SET esta vacio"
    else:
        sale = f"Error en dato {dato_info} es del tipo {type(dato_info)}"
    return sale


def leer(mensaje : str, tipo : int) -> str:
    try:
        if tipo == 1:
            entrada = int(input(f"{mensaje}"))
        elif tipo == 2:
            entrada = input(f"{mensaje}")
        elif tipo == 3:
            entrada = float(input(f"{mensaje}"))
        elif tipo == 4:
            entrada = bool(input(f"{mensaje}"))
        else:
            print("Error en Tipo de Datos ")
    except ValueError:
        entrada = 0
        if tipo == 1:
            print("El Valor Ingresado no es un entero ")
        elif tipo == 2:
            print("El Valor Ingresado no es un string ")
            entrada = ""
        elif tipo == 3:
            print("El Valor Ingresado no es un Boleano ")
        elif tipo == 4:
            print("El Valor Ingresado no es un Numero con decimales ")
        
    return entrada

def leer_1(mensaje : str, tipo : int) -> str:
    while True:
        entrada = input(f"{mensaje}")
        #print(f"\nValor del tipo @{type(entrada)}@")
        if   tipo == 1 and type(int(entrada)) != int:
            print("El Valor Ingresado no es un entero")
        elif tipo == 2 and type(entrada) != str:
            print("El Valor Ingresado no es un string")
        elif tipo == 3 and type(float(entrada)) != float:
            print("El Valor Ingresado no es un Numero con decimales")
        elif tipo == 4 and type(bool(entrada)) != bool:
            print("El Valor Ingresado no es un Numero con decimales")
        else:
            if tipo == 1:
                if entrada.isdigit(): 
                    entrada = int(entrada) 
                else:
                    entrada = 0
                    print ("Error en tipo de dato")
            elif tipo == 3:
                entrada = float(entrada)
            break

    return entrada

def ingreso_empleado(id):
    nombre  = ""
    edad    = 0
    sexo    = ""
    dni     = 0
    trabaja = 9
    confirma = "N"
    largomax = 15
    while len(nombre)==0 or len(nombre) > largomax:
        nombre  =     leer("Nombre   : ", 2)
        if len(nombre)>largomax:
            nombre = nombre[:largomax]
            print(f"El nombre quedará : {nombre}")
            confirma = ""
            while confirma != "N" and confirma != "S":
                confirma = leer("Confirma cortar el nombre ? S=SI N=NO : ", 1)
            if confirma == "N":
                nombre = ""
    while edad < 1 or edad > 120:
        edad    = leer("Edad     : ", 1)
    while sexo != "Masculino" and sexo != "Femenino":
        sexo    =     leer("Sexo     : ", 2)
        if sexo=="M":
            sexo = "Masculino"
        elif sexo == "F":
            sexo = "Femenino"

    sexo    = True if sexo == "Masculino" else False
    while dni <= 0 or dni >= 99000000:
        dni     = leer("D.N.I.   : ", 1)

    while trabaja < 0 or trabaja > 1:
        trabaja = input("Trabaja 0=NO 1=SI : ")
        if trabaja.isdigit():
            trabaja = int(trabaja)
        else:
            trabaja = 9
            print("Valor inválido")
    trabaja = bool(trabaja)
    sueldo = 0.0
    if trabaja:
        while sueldo <= 0:
            sueldo = leer("Sueldo   : ", 3)

    agregar_empleado = { id : (nombre, edad, sexo, dni, trabaja, sueldo) }
    return agregar_empleado

def formatear_id(id : str, largo : int) -> str:
    texto = "0"*3+id
    salida = texto[-largo:]
    return salida
