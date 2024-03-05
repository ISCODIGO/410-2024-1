with open("test.txt", mode="a") as manejador:
    for x in range(100):
        manejador.write(str(x))
        manejador.write("\n")
