"""
Ejercicio 2: Escribe un programa que solicite un nombre de archivo
y después lea ese archivo buscando las líneas que tengan la siguiente
forma:
X-DSPAM-Confidence: 0.8475
**Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla
aparte para extraer el número decimal de la línea. Cuenta esas líneas y después
calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al
final del archivo, imprime el valor medio de “spam confidence”.
Ingresa un nombre de archivo: mbox.txt
Promedio spam confidence: 0.894128046745
Ingresa un nombre de archivo: mbox-short.txt
Promedio spam confidence: 0.750718518519
"""

# Solicitar el archivo
archivo = input("Escriba el nombre del archivo: ")

# Leer el archivo
try:
    manejador = open(archivo)
except FileNotFoundError:
    print("Archivo no se encuentra")
else:
    confianza_total = 0  # total de confianza
    lecturas = 0  # elementos leidos
    for linea in manejador:
        if linea.startswith("X-DSPAM-Confidence:"):
            tokens = linea.split()  # Divide la linea en palabras
            confianza = float(tokens[1])
            confianza_total += confianza
            lecturas += 1
    print("El promedio de confianza es:", confianza_total / lecturas)
