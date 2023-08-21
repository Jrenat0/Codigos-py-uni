class Hora():
    def __init__(self):       
        self.hora= int
        self.minu= int
        

class Alumno():
    def __init__(self):    
        self.nombre = str
        self.nota = int
        self.horaini = Hora()
        self.horafin = Hora()
    
class TempoAlumno():
    def __init__(self):
        self.nombre = str
        self.nota = int
        self.tiempo = int
        
        

def calculartiempo(self):
    tiempo = (self[i].horafin.hora*60+self[i].horafin.minu)-(self[i].horaini.hora*60+self[i].horaini.minu)
    return tiempo



n = int(input("Ingrese el numero de alumnos: "))
alumnos = [Alumno() for i in range(n)]
resul = [TempoAlumno() for i in range(n)]

for i in range(n):
    alumnos[i].nombre = input("Ingrese su nombre: ")
    alumnos[i].nota = int(input("Ingrese su nota: "))
    alumnos[i].horaini.hora = int(input("Ingrese la hora de inicio de su examen: "))
    alumnos[i].horaini.minu = int(input("Ingrese los minutos de inicio de su examen: "))
    alumnos[i].horafin.hora = int(input("Ingrese la hora de final de su examen: "))
    alumnos[i].horafin.minu = int(input("Ingrese la minutos de final de su examen: "))


for i in range(n):
    resul[i].nombre = alumnos[i].nombre
    resul[i].nota = alumnos[i].nota
    resul[i].tiempo = calculartiempo(alumnos)

for i in range(n):
    print(resul[i].nombre)
    print(resul[i].nota)
    print(resul[i].tiempo)