'''
# Opcion 1
import carta
c = carta.Carta()
'''

from carta import Carta
from jugador import Jugador


c1 = Carta("Diamantes", "As")
c2 = Carta("Corazones", 9)
c3 = Carta("Corazones", 5)

a = Jugador("Alfa")
print(a)
a.pedir_carta(c1)
a.pedir_carta(c2)
a.pedir_carta(c3)
print("Puntos:", a.sumar_mano())

from baraja import Baraja
b = Baraja()