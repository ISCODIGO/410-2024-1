manejador = open("mbox-short.txt")
print(manejador)

# Lectura por caracteres (todo el archivo)
'''caracteres = manejador.read()
print("Caracteres:", len(caracteres))
print("Primer elemento: ", caracteres[0])'''

# Lectura por lineas (todo el archivo)
'''lineas = manejador.readlines()
print("Lineas:", len(lineas))
print("Primera linea:", lineas[0])'''

# Lectura por linea
print("Primera linea:", manejador.readline())
print("Segunda linea:", manejador.readline())

linea = manejador.readline()
while linea:
    print(linea)
    linea = manejador.readline()  # actualizar la linea


