import sqlite3


conn = sqlite3.connect("test.db")

cursor = conn.cursor()
cursor.execute("drop table if exists alumnos")
cursor.execute("create table alumnos(cuenta TEXT, nombre TEXT, carrera TEXT) ")
conn.close()
