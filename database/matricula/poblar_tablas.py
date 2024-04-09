'''
CRUD ... C = create

'''
import sqlite3
from constantes import DB_NOMBRE


conn = sqlite3.connect(DB_NOMBRE)

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS alumnos")
cursor.execute("""
    CREATE TABLE "alumnos" (
        "cuenta"	TEXT NOT NULL UNIQUE,
        "nombre"	TEXT NOT NULL,
        "carrera"	TEXT NOT NULL,
        "id"	INTEGER NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    )
""")
cursor.execute("""
    insert into alumnos(cuenta, nombre, carrera)
    values('202310011213', 'Jaime Valeriano', 'Medicina')
""")
cursor.execute("""
    insert into alumnos(cuenta, nombre, carrera)
    values('202310011214', 'Andrea Alves', 'Derecho')
""")
cursor.execute("""
    insert into alumnos(cuenta, nombre, carrera)
    values('202310011215', 'Alan Lopez', 'Arquitectura')
""")
conn.commit()
conn.close()
