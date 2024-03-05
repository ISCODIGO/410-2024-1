"""
Crear un programa que lea el archivo ventas.csv y genera la suma total.
"""
with open("ventas.csv") as archivo:
    total = 0
    for lineas in archivo:
        tokens = lineas.split(",")
        try:
            total += float(tokens[2])
        except ValueError:
            pass
    print("Venta total:", total)