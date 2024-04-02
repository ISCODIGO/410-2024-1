class Alumno:
    def __init__(self, nombre, cuenta, carrera):
        self.nombre = nombre
        self.cuenta = cuenta
        self.carrera = carrera

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Carrera: {self.carrera}"
