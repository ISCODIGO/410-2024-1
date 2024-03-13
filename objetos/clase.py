class Persona:
    cantidad = 121

    def __init__(self, cantidad) -> None:
        self.cantidad += cantidad

    def probar(self):
        Persona.cantidad = 100


per = Persona(10)
print(per.cantidad)
per.probar()
print(per.cantidad)
print(per.__dict__)
print(Persona.__dict__)
