import sqlite3


conexion = sqlite3.connect("test.db")
cursor = conexion.cursor()

cuenta = input("Seleccionar una cuenta: ")
cursor.execute("select * from alumnos where cuenta = ?", (cuenta, ))
dato = cursor.fetchone()
print(dato)
