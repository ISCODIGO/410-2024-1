import sqlite3


conn = sqlite3.connect("test.db")

cursor = conn.cursor()
cursor.execute("""
delete from alumnos
""")
conn.commit()
conn.rollback()
conn.close()
