from enum import Enum
from baraja import Baraja
from carta import Carta
from jugador import Jugador, EstadoJugador
from colorterminal import ColorTerminal


class EstadoJuego(Enum):
    INICIA = 0
    CONTINUA = 1
    FINALIZA = 2


class Juego:
    def __init__(self) -> None:
        self.baraja = Baraja()
        self.jugadores = list()
        self.estado = EstadoJuego.INICIA

    def crear_jugadores(self):
        """
        Inicializa los jugadores
        """
        c = int(input("Cuantos jugadores [1-4]: "))
        for x in range(c):
            nombre = input(f"Nombre del jugador-{x}: ")
            self.jugadores.append(Jugador(nombre))

    def _pasar_carta(self, j: Jugador) -> Carta:
        """
        Obtiene la carta actual de la baraja y la entrega al jugador
        """
        carta = self.baraja.dar_carta()
        j.pedir_carta(carta)
        return carta

    def _buscar_blackjack(self) -> Jugador | None:
        """
        Retorna al jugador que tiene blackjack
        TODO: es posible que exista mas de un jugador con blackjack.
        """
        for j in self.jugadores:
            j: Jugador
            if j.estado == EstadoJugador.BLACKJACK:
                return j
        return None

    def _buscar_ganador(self) -> Jugador:
        """
        Revisa entre todos los jugadores si hay un jugador con 21 o
        su defecto tiene la mayor cantidad sin pasarse.
        TODO: Agregar opcion que en caso de empate gane quien tiene menos
        cartas en su mano.
        """

        candidatos = [j for j in self.jugadores if j.puntos <= 21]

        if candidatos:
            return max(candidatos)

        return None

    def ronda(self):
        """
        Primer parte:
        - Se lanzan dos cartas a cada jugador.
        - Al final de la ronda se determina si hay BLACKJACK (21).

        Segunda parte:
        - En caso de no existir ganador, cada jugador indica si se planta
        o continua recibiendo cartas. Si el jugador recibe mas de 21,
        pierde de inmediato.
        - Una vez ya todos los jugadores se plantaron o perdieron, se revisa
        el jugador con el mayor puntaje sin pasarse.
        - Si hay empate revisar el que tenga menos cartas.
        """
        # Primera ronda
        for j in self.jugadores:
            self._pasar_carta(j)
            self._pasar_carta(j)
        ganador = self._buscar_blackjack()
        if ganador:
            self.estado = EstadoJuego.FINALIZA
        else:
            self.estado = EstadoJuego.CONTINUA

        # Segunda ronda
        while self.estado == EstadoJuego.CONTINUA:
            for j in self.jugadores:
                j: Jugador  # Acceder a atributos y metodos desde el editor
                print("Jugador:", j)
                while j.estado == EstadoJugador.ACTIVO:
                    opcion = input("\t[Q] Quedarse [P] Pedir carta: ").lower()

                    if opcion == "q":
                        j.plantarse()
                    else:  # accion por defecto
                        carta = self._pasar_carta(j)
                        print(f"\t{carta}... {j.puntos}")
            self.estado = EstadoJuego.FINALIZA

        # Determinar si hay ganador
        ganador = self._buscar_ganador()
        if ganador:
            self.generar_tabla(ganador)
            self.estado = EstadoJuego.FINALIZA

    def generar_tabla(self, ganador: Jugador):
        """
        Funcion para mostrar los detalles de las cartas en la pantalla.
        """
        linea_h = []
        header = []
        contenido = {}
        max_fila_cartas = max(len(j.mano) for j in self.jugadores)
        max_columna_cartas = max(len(str(c)) for j in self.jugadores for c in j.mano)
        for j_index, j in enumerate(self.jugadores):
            j: Jugador
            jugador_str = str(j)
            ancho_jugador = len(jugador_str) + 2
            ancho_columna = max(ancho_jugador, max_columna_cartas)

            if j == ganador:
                jugador_str = ColorTerminal.to_str(jugador_str, ColorTerminal.GREEN)
            elif j.estado == EstadoJugador.PIERDE:
                jugador_str = ColorTerminal.to_str(jugador_str, ColorTerminal.RED)

            if j_index == 0:
                primer_linea_h = "+"
                primer_header = "| "
            else:
                primer_linea_h = ""
                primer_header = " "
            linea_h.extend([primer_linea_h, "-" * ancho_columna, "+"])
            header.extend([primer_header, jugador_str, " |"])
            for index in range(max_fila_cartas):
                try:
                    carta_str = str(j.mano[index])
                except IndexError:
                    carta_str = ""
                margen = ancho_columna - len(carta_str) - 1
                if index not in contenido:
                    contenido[index] = []
                contenido[index].extend([primer_header, carta_str, " " * margen, "|"])

        print("".join(linea_h))
        print("".join(header))
        print("".join(linea_h))
        for v in contenido.values():
            print("".join(v))
        print("".join(linea_h))
