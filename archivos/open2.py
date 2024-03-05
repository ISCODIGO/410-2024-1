with open("mbox-short.txt") as manejador:
    """
    Con el manejador de contexto with se permite que el recurso una vez concluya su
    lectura se cierre.
    """
    for linea in manejador:
        print(linea)
