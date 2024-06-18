"""Prueba_3"""
import csv
opc = 0
# esto es parea crear el archivo solamente
# with open("pedidos.csv", "w", newline="") as archivo_csv:
#  escritor = csv.writer(archivo_csv)
# escritor.writerow(["Cliente", "Dirección", "Sector", "Cil. 5kg", "Cil. 15kg", "Cil. 45kg"])

def Registrar_pedido():
    print("Por favor ingrese los datos..")
    while True:
        Cliente = input("Ingrese su Nombre y apellido: ")
        if " " in Cliente:
            print("")
            break
        else:
            print(
                "Hubo un error intente nuevamnete, Nombre y pellido ejemplo: Juan Pedraza")
    while True:
        dirreccion = input("Ingrese su dirección: ")
        print("Es correcta su dirección? ")
        print("elija una opción numerica..")
        seguro = 0
        try:
            seguro = int(input("1. si / 2. no: "))
        except ValueError:
            print("Intente ingresar nuevamente..")
            seguro = 0
        if seguro == 1:
            print()
            break
        else:
            print("Intente nuevamente")
    while True:
        print("SECTORES: Centro, Colina, Industrias.")
        sector = input("Ingrese su sector: ").title()
        if sector == "Centro" or sector == "Colina" or sector == "Industrias":
            print()
            break
        else:
            print("Intente nuevamente, elija un sector definido")
    while True:
        print("Ingrese cuantos cilindros quiere llevar ")
        try:
            print("Cuantos de Cil. 5kg quiere llevar?")
            cil_5 = int(input("ingrese: "))
            print("Cuantos de Cil. 15kg quiere llevar?")
            cil_15 = int(input("ingrese: "))
            print("Cuantos de Cil. 45kg quiere llevar?")
            cil_45 = int(input("ingrese: "))
            break
        except ValueError:
            print("Hubo un error intente nuevamente")
    with open("pedidos.csv", "a", newline="") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerows([
            [Cliente, dirreccion, sector, cil_5, cil_15, cil_45]
        ])
        print("Guardado Correctamente...")


def lista_pedidos():
    with open("pedidos.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            print(fila)


def imprimir_hoja():
    lista_texto = []
    with open("pedidos.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        print("Seleccióne un sector...")
        print("SECTORES: Centro, Colina, Industrias.")
        sector_buscar = input("Ingrese su sector: ").title()
        print(f"Aqui estan los datos del sector: {sector_buscar}")
        for fila in lector:
            if sector_buscar in fila:
                lista_texto.append(fila)
            else:
                print
        else:
            print()
    with open("archivo.txt", "w", newline="") as archivo_txt:
        archivo_txt.write(str(lista_texto))

    with open("archivo.txt", "r", newline="") as archivo_txt:
        lector = archivo_txt.read()
        print(lector)


while True:
    print("""
        Gaxplosive
          
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Salir del programa
    """)
    try:
        opc = int(input("Ingrese una Opción: "))
    except ValueError:
        print("Hubo un error, por favor intente nuevamente...")
        opc = 0

    if opc == 1:
        Registrar_pedido()
    elif opc == 2:
        lista_pedidos()
    elif opc == 3:
        imprimir_hoja()
    elif opc == 4:
        print("Cerrando...")
        break
    else:
        print()
