'''

cR(read)ud

'''

import sqlite3
from pprint import pprint


conn = sqlite3.connect("test.db")

cursor = conn.cursor()
cursor.execute("""
    select *
    from alumnos
""")
dato = cursor.fetchall()
pprint(dato)
conn.close()
