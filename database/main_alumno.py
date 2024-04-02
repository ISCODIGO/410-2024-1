from alumno import Alumno
from alumno_db import AlumnoDB

'''
alumno = Alumno("Oscar", "8901", "Odontologia")
db = AlumnoDB(alumno)
db.create()
'''

alumno2 = Alumno("Enrique", "Ing. Sistemas", "")
db2 = AlumnoDB(alumno2)
db2.delete()
