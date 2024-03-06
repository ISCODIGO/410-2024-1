import random
from carta import Carta


class Baraja:
    def __init__(self) -> None:
        self.baraja = [None] * 52  # una lista con 52 espacios None
        self.actual = 0  # lleva el recuento de la carta que sigue
        index = 0
        for fig in Carta.FIGURAS:
            for val in Carta.VALORES:
                # print(index, fig, val)
                self.baraja[index] = Carta(valor=val, figura=fig)
                index += 1

    def mezclar(self):
        """
        Ordenar aleatoriamente las 52 cartas de la baraja
        """
        self.actual = 0
        for index, _ in enumerate(self.baraja):
            aleatorio = random.randint(0, 51)
            self.baraja[index], self.baraja[aleatorio] = (
                self.baraja[aleatorio],
                self.baraja[index],
            )

    def pedir(self):
        """
        Aumentar el valor de [actual] en 1.
        Devolver la carta perteneciente a la posicion de [actual]
        """

        if self.actual == len(self.baraja) - 1:
            print("** Nueva baraja")
            self.mezclar()

        carta = self.baraja[self.actual]
        self.actual += 1
        return carta
