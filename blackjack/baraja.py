from carta import Carta

class Baraja:
    def __init__(self) -> None:
        self.baraja = [None] * 52  # una lista con 52 espacios None
        for index, _ in enumerate(self.baraja):
            for fig in Carta.FIGURAS:
                for val in Carta.VALORES:
                    print(index, fig, val)
                    self.baraja[index] = Carta(valor=val, figura=fig)

        for carta in self.baraja:
            print(carta)
