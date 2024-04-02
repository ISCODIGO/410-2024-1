from db import Database
from alumno import Alumno


class AlumnoDB(Database):
    def __init__(self, alumno: Alumno) -> None:
        super().__init__("test.db")
        self.alumno = alumno

    def create(self):
        self.open()
        self.cursor.execute(
            """INSERT INTO alumnos(nombre, cuenta, carrera)
        VALUES(?, ?, ?)
        """,
            (self.alumno.nombre, self.alumno.cuenta, self.alumno.carrera),
        )
        self.connection.commit()
        self.connection.close()

    def read(self):
        self.open()
        self.cursor.execute(
            "SELECT * FROM alumnos WHERE cuenta = ?", (self.alumno.cuenta)
        )
        data = self.cursor.fetchone()
        self.connection.close()
        return data

    def update(self):
        self.open()
        self.cursor.execute(
            """UPDATE alumnos SET carrera = ?
            WHERE cuenta = ?
        """,
            (self.alumno.carrera, self.alumno.cuenta),
        )
        self.connection.commit()
        self.connection.close()

    def delete(self):
        self.open()
        self.cursor.execute(
            """DELETE FROM alumnos
            WHERE cuenta = ?
        """,
            (self.alumno.cuenta,),
        )
        self.connection.commit()
        self.connection.close()
