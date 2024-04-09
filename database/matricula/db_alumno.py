from db import Database
from alumno import Alumno
from constantes import DB_NOMBRE


class AlumnoDB(Database):
    def __init__(self, alumno: Alumno) -> None:
        super().__init__(DB_NOMBRE)
        self.alumno = alumno

    def create(self):
        super().create(
            """INSERT INTO alumnos(nombre, cuenta, carrera)
        VALUES(?, ?, ?)
        """,
            (self.alumno.nombre, self.alumno.cuenta, self.alumno.carrera),
        )

    def read(self):
        return super().read(
            "SELECT * FROM alumnos WHERE cuenta = ?", (self.alumno.cuenta)
        )

    def update(self):
        super().update(
            """UPDATE alumnos SET carrera = ?
            WHERE cuenta = ?
        """,
            (self.alumno.carrera, self.alumno.cuenta),
        )

    def delete(self):
        super().delete(
            """DELETE FROM alumnos
            WHERE cuenta = ?
        """,
            (self.alumno.cuenta,),
        )
