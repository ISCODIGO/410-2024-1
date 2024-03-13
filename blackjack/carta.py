from enum import Enum


class Figura(Enum):
    CORAZON = "♥"
    ESPADA = "♠"
    DIAMANTE = "♦"
    TREBOL = "♣"


class Carta:
    VALORES = {
        "A": 11,
        "DOS": 2,
        "TRES": 3,
        "CUATRO": 4,
        "CINCO": 5,
        "SEIS": 6,
        "SIETE": 7,
        "OCHO": 8,
        "NUEVE": 9,
        "DIEZ": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    def __init__(self, figura: Figura, valor: str):
        self.figura = figura
        self.valor = valor  # Esto llamará al setter de valor.

    @property
    def valor(self):
        return str(self._valor).upper()

    @valor.setter
    def valor(self, value):
        if value not in Carta.VALORES:
            raise ValueError(f"Valor '{value}' inválido.")
        self._valor = value

    def get_valor(self):
        """
        Devuelve el valor numérico de la carta.
        """
        return Carta.VALORES.get(self._valor, self._valor)

    def __str__(self) -> str:
        return f"{self.valor} {self.figura.value}"
