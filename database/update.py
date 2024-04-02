import sqlite3


conn = sqlite3.connect("test.db")

cursor = conn.cursor()
cursor.execute("""
update alumnos set carrera='Enfermeria'
where cuenta='202310011213'
""")
conn.commit()
conn.close()
