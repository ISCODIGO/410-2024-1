"""
Crear un programa que captura la fecha (str), ciudad y venta hasta que el usuario indique que
termina la carga. Luego convertir esos datos en un archivo CSV (separado por comas).
"""
def cargar_datos(datos: dict):
    fecha = input("Fecha: ")
    ciudad = input("Ciudad: ")
    venta = input("Venta: ")  # se puede validar previamente
    datos[(fecha, ciudad)] = venta

def escribir_archivo(datos: dict):
    with open("ventas.csv", mode="w") as archivo:
        archivo.write("Fecha,Ciudad,Venta\n")  # encabezado del archivo
        for clave, valor in datos.items():
            # recordar que la clave es una tupla: (fecha, ciudad)
            (fecha, ciudad) = clave
            archivo.write(f"{fecha},{ciudad},{valor}\n")  # contenido del archivo

# Crear un menu basico
entrada = None
repositorio = dict()
while (entrada != "2"):
    print("MENU")
    print("1. Cargar datos")
    print("2. Terminar la carga")
    entrada = input("> ")
    match entrada:
        case "1":
            cargar_datos(repositorio)
        case "2":
            print("Carga terminada...")
        case _:
            print("Opcion invalida, intente de nuevo")
escribir_archivo(repositorio)