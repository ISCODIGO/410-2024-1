def crear_menu(titulo: str, lista: list):
    opciones = 0
    print(titulo)
    for item in lista:
        print(f"{opciones}. {item}")
        opciones += 1
    resultado = int(input())
    return resultado


with open("open.py") as archivo:
    linea = archivo.readline()  # "Fecha,Ciudad,Venta"
    header = linea.split(",")  # ["Fecha", "Ciudad", "Venta"]
    opcion = crear_menu("Buscar por:", header)
    print("Usted escogio la opcion:", header[opcion])

    