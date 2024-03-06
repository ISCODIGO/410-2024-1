from baraja import Baraja
from jugador import Jugador

class Juego:
    def __init__(self) -> None:
        self.baraja = Baraja()
        self.baraja.mezclar()
        self.jugadores = list()

    def crear_jugadores(self):
        c = int(input("Indica la cantidad de jugadores:"))
        for x in range(c):
            nombre = input("Escriba el nombre del jugador", x)
            self.jugadores.append(Jugador(nombre))
