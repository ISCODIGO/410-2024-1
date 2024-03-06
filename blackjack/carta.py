class Carta:
    FIGURAS = (
        "Corazones",
        "Treboles",
        "Diamantes",
        "Espadas",
    )

    VALORES = (
        "As",
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        "J",
        "Q",
        "K",
    )

    def __init__(self, figura: str, valor: str):
        self.figura = figura
        self.valor = valor
        self.valor_numerico = None

    @property
    def figura(self):
        return str(self._figura).upper()

    @figura.setter
    def figura(self, value):
        if value not in Carta.FIGURAS:
            raise ValueError(f"{value} es invalido como figura")

        self._figura = value

    @property
    def valor(self):
        return str(self._valor).upper()

    @valor.setter
    def valor(self, value):
        if value not in Carta.VALORES:
            raise ValueError(f"{value} es un invalido como valor")

        self._valor = value

    def get_valor(self):
        """
        De acuerdo al valor de la carta devolver su valor numerico:
        As -> 11
        J, Q, K -> 10
        """
        if self._valor == "As":
            return 11

        if self._valor in ["J", "Q", "K"]:
            return 10

        try:
            return int(self._valor)
        except TypeError:
            raise ValueError("Valor indefinido")

    def __str__(self) -> str:
        return f"{self.valor}-{self.figura}"
