class Persona:
    nombre = None
    edad = 0
    profesion = None

    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentar(self):
        return f"Hola, me llamo {self.nombre} y mi profesion es {self.profesion}. Tengo {self.edad} años."


persona = Persona("Alfredo", "25", "Medico")
persona.presentar()


class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion):
        super().__init__(nombre, edad, profesion)
        self.cursos = []

    def estudiar(self, pos: int):
        try:
            print(f"Esta estudiando: {self.cursos[pos]}")
        except IndexError:
            print("Error")

    def matricular(self, curso):
        if len(self.cursos) == 5:
            print("No puede matricular otro curso")
        else:
            self.cursos.append(curso)
            print(f"Curso agregado: {curso}")


estudiante = Estudiante("Manuel", 19, "Tecnico Radiologia")
estudiante.matricular("Anatomia")
estudiante.matricular("Ingles I")
estudiante.estudiar(0)


class Prueba:
    nombre = None

    def algo(self):
        self.variable = 10


p = Prueba()
p.nombre = "Javier"
