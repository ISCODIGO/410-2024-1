import sqlite3


nombre = input("Ingrese un nombre: ")
carrera = input("Ingrese una carrera: ")
cuenta = input("Ingrese la cuenta: ")


conexion = sqlite3.connect("test.db")
cursor = conexion.cursor()
cursor.execute("""
insert into alumnos(nombre, cuenta, carrera)
values(?, ?, ?)
""", (nombre, cuenta, carrera))
conexion.commit()
conexion.close()
