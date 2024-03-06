class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.creditos = 500
        self.mano = []
        self.continuar = True

    def __str__(self) -> str:
        return f"{self.nombre}({self.creditos})"

    def quedarse(self):
        self.continuar = False

    def pedir_carta(self, carta):
        self.mano.append(carta)

    def sumar_mano(self):
        total = 0
        ases = 0
        for carta in self.mano:
            if carta.valor == "AS":
                ases += 1
            total += carta.get_valor()

        if total > 21 and ases > 0:
            total = total - 10
            # TODO: que pasa si hay varios As y se sigue pasando
        return total
