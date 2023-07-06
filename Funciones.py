import os 
import time
import numpy

#Mostrar menu y validar opcion:

def mostrar_menu():
    print("""Bienvenido a Creativos.cl seleccione opcion
    1. Comprar entrada
    2. Mostrar ubicaciones dispónibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("Opcion invalida")
        except:
            print("ERROR! Debe ingresar un numero entero")

#Validar rut:

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin guion ni digito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("Rut ingresado invalido!!")
        except:
            print("ERROR! Debe ingresar un numero entero")

#Variables_necesarias:

escenario = numpy.zeros((10,10), int)



listas_ruts = []
listas_totales = []
listas_filas = []
listas_columnas = []
listas_cant_entradas = []


#ver esceanario:

def ver_escenario():
    os.system('clear')
    print("ESCENARIO")
    for x in range(10):
        print(f"FILA {(x+1)}:", end=" ")
        for y in range(10):
            print(f"{escenario[x][y]}", end=" ")
        print()
    print("Columna  a b c d e f g h i j ")
    time.sleep(3)

#validar cantidad entradas:

def cantidad_entradas():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas que desea comprar(1-3): "))
            if cantidad >= 1 and cantidad <= 3:
                return cantidad
            else:
                print("Cantidad ingresada invalida!!")
        except:
            print("ERROR!! Debe ingresar un numero entero")

#Validar fila y columna: 

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("Fila invalida!!")
        except:
            print("ERROR!! Debe ingresar un numero entero")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna in ("a","b","c","d","e","f","g","h","i","j"):
                return columna
            else:
                print("Columna ingresada invalida!!")
        except:
            print("ERROR!! Debe ingresar un numero entero")

#Validar_menu:

def ver_menu_entradas():
    os.system('clear')
    print("""ENTRADAS: 
    1. Platinum:  $120.000(asientos del 1 al 20)
    2. Gold:      $80.000(asientos del 21 al 50)
    3. Silver:    $50.000(asientos del 51 al 100)""")

def validar_opc_entra():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3):
                return opcion
            else:
                print("Opcion invalida")
        except:
            print("ERROR! Debe ingresar un numero entero")

def comprar_entradas():
    rut = validar_rut()
    if rut not in listas_ruts:
        print("NO existe rut indicado")
        time.sleep(3)
        return
    acumulador = 0
    ver_menu_entradas()
    opcion = validar_opc_entra()
    while True:
            if opcion==1:
                while True:
                    try:
                        cantidad_pla = int(input("Ingrese cantidad de platinum que desea: "))
                        if cantidad_pla >= 1 and cantidad_pla <=3 :
                            return cantidad_pla
                        else:
                            print("ERROR!! cantidad invalida")
                    except:
                        print("ERROR!! Debe ingresar un numero entero")
                        acumulador = acumulador + 120000*cantidad_pla

            elif opcion==2:
                while True:
                    try:
                        cantidad_gold = int(input("Ingrese cantidad de gold que desea: "))
                        if cantidad_gold >= 1 and cantidad_gold <=3 :
                            return cantidad_gold
                        else:
                            print("ERROR!! cantidad invalida")
                    except:
                        print("ERROR!! Debe ingresar un numero entero")
                        acumulador = acumulador + 80000*cantidad_gold

            else:
                while True:
                    try:
                        cantidad_silver = int(input("Ingrese cantidad de silver que desea: "))
                        if cantidad_silver >= 1 and cantidad_silver <=3 :
                            return cantidad_silver
                        else:
                            print("ERROR!! cantidad invalida")
                    except:
                        print("ERROR!! Debe ingresar un numero entero")
                        acumulador = acumulador + 50000*cantidad_silver

def reservar_entrada():
    print("RESERVAR")
    rut = validar_rut()
    if rut in listas_ruts:
        print("Ya tiene una reserva")

    cantidad = cantidad_entradas()
    fila = validar_fila()
    columna = validar_columna()

    if escenario[fila-1][columna-1] == 0:
        escenario[fila-1][columna-1] = 1
        listas_filas.append(fila-1)
        listas_ruts.append(rut)
        listas_columnas.append(columna-1)
        listas_totales.append(0)
        listas_cant_entradas.append(cantidad)
        print("reservado con exito")
    else:
        print("Guardias!!")

#ver listado de clientes:
def buscar():
    rut = validar_rut()
    posicion = listas_ruts.index(rut)
    if rut in listas_ruts:
        print("Listado de asistentes: ", listas_ruts.index[posicion])
    else:
        print("Rut no registrado")

#mostrar ganancias totales:
def ganancias():
    print("GANANCIAS TOTALES: ")
    rut = validar_rut
    if rut in listas_ruts:
        posicion = listas_ruts.index(rut)
        print(f"""GANANCIAS
        tipo entrada           cantidad       total
        Platinum         {listas_cant_entradas} {listas_totales}
        Gold             {listas_cant_entradas}  {listas_totales}
        Silver           {listas_cant_entradas}  {listas_totales} 
        TOTAL            {listas_cant_entradas}  {listas_totales}""")

        fila = listas_filas[posicion]
        columna = listas_columnas[posicion]
        escenario[fila-1][columna-1] = 0

        listas_ruts.pop(posicion)
        listas_filas.pop(posicion)
        listas_columnas.pop(posicion)
        listas_totales.pop(posicion)
        print("Pago con exito!!")
    else:
        print("EL RUT INDICADO NO SE ENCUENTRA REGISTRADO!!")
