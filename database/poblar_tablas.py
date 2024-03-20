'''
CRUD ... C = create

'''
import sqlite3


conn = sqlite3.connect("test.db")

cursor = conn.cursor()
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
