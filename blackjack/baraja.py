import random
from carta import Carta, Figura


class Baraja:
    def __init__(self) -> None:
        self.baraja = [None] * 52  # una lista con 52 espacios None
        self.actual = 0  # lleva el recuento de la carta a entregar
        index = 0
        for val in Carta.VALORES:
            for figura in Figura:
                self.baraja[index] = Carta(valor=val, figura=figura)
                index += 1

        self._mezclar()

    def _mezclar(self):
        """
        Ordenar aleatoriamente las 52 cartas de la baraja
        """
        random.shuffle(self.baraja)
        self.actual = 0

    def dar_carta(self) -> Carta:
        """
        Retorna la carta [actual] moviendose a la siguiente
        """
        # En caso de finalizar la baraja la mezcla de nuevo
        if self.actual == len(self.baraja) - 1:
            self._mezclar()

        carta = self.baraja[self.actual]
        self.actual += 1
        return carta
