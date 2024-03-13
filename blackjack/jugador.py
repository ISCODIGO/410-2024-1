from enum import Enum


class EstadoJugador(Enum):
    ACTIVO = 0
    PLANTADO = 1
    PIERDE = 2
    BLACKJACK = 3


class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.creditos = 500
        self.mano = []
        self.estado = EstadoJugador.ACTIVO
        self._puntos = 0

    def __str__(self) -> str:
        return f"{self.nombre}({self.puntos})"

    def plantarse(self):
        """
        Funcion para dejar de pedir cartas
        """
        self.estado = EstadoJugador.PLANTADO

    def pedir_carta(self, carta):
        """
        Funcion para recibir una carta
        """
        self.mano.append(carta)
        self.actualizar_puntos()

    def actualizar_puntos(self):
        """
        Funcion para actualizar el puntaje y el estado del jugador.
        """
        self._puntos = sum(carta.get_valor() for carta in self.mano)

        if self.is_blackjack():
            self.estado = EstadoJugador.BLACKJACK

        ases = sum(1 for carta in self.mano if carta.valor == "A")
        while self._puntos > 21 and ases > 0:
            self._puntos -= 10
            ases -= 1
        # Verificar si el jugador se pasa de 21 puntos
        if self._puntos > 21:
            self.estado = EstadoJugador.PIERDE

    @property
    def puntos(self):
        return self._puntos

    def is_blackjack(self) -> bool:
        return self.puntos == 21

    # Métodos de comparación
    def __eq__(self, other) -> bool:  # self == other
        return self.puntos == other.puntos and self.nombre == other.nombre

    def __ne__(self, other) -> bool:  # self != other
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:  # self < other
        return self.puntos < other.puntos

    def __le__(self, other) -> bool:  # self <= other
        return self.__lt__(other) or self.puntos == other.puntos

    def __gt__(self, other) -> bool:  # self > other
        return self.puntos > other.puntos

    def __ge__(self, other) -> bool:  # self >= other
        return self.__gt__(other) or self.puntos == other.puntos
