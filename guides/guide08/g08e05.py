#5) Implementar la clase Asignatura que represente el nombre de una asignatura y la nota correspondiente obtenida. Las operaciones
#  son:
#Constructor que acepte como parámetros el nombre de la asignatura y la nota obtenida.
#Métodos para modificar la nota (setNota) y para consultar la nota (getNota).
#Método que nos devuelva “Aprobado” si la nota es mayor o igual a 4 o “Reprobado” si la nota es menor que 4.
#Método para consultar el nombre de la asignatura.
#Implementar la clase Alumno que incluya una coleccion de Asignaturas a las que el alumno ha asistido. Ademas de incluir los
#  atributos nombre y edad. Las operaciones disponibles sobre el alumno son:
#Constructor que acepte como parámetro el nombre del alumno y edad.
#Métodos para modificar el nombre (setNombre) y para consultarlo (getNombre).
#Métodos para modificar y consultar la edad.
#Método que nos devuelva el promedio del alumno.
#Método para agregar una Asignatura a su plan de estudio; verificar que la asignatura no exista previamente en el arreglo de este
#  Alumno.
#Implementar la clase Aplicación para hacer uso de las clases Alumno y Asignatura.
#Crear 3 alumnos (Tres instancias de la clase Alumno) con sus respectivos nombre y edad.
#Para cada alumno establecer sus asignaturas y la nota obtenida.
#Imprimir en pantalla:
#1.Nombre del alumno.
#2.Edad.
#3.Asignaturas que cursó:
#Nombre de la asignatura.
#Nota obtenida.
#Si es una asignatura aprobada o no.
#4.Promedio del alumno
class Asignature():
    def __init__(self,asigName='',asigNote=''):
        self.asigName = asigName
        self.asigNote = asigNote
    def setNote(self,newNote):
        self.asigNote = newNote
    def getNote(self):
        if self.asigNote != '':
            return self.asigNote
        return 'Do you havent note here'
    def asigState(self):
        if self.asigNote != '':
            return 'Approved' if self.asigNote >= 4 else 'Dissaproved'
        return 'Do you havent note here'
    def getAsigName(self):
        return self.asigName

class Student():
    def __init__(self,name,age,asignatures):
        self.name = name
        self.age = age
        self.asignatures = asignatures
    def setName(self,newName):
        self.name = newName
    def getName(self):
        return self.name
    def setAge(self,newAge):
        self.age = newAge
    def getAge(self):
        return self.age
    def getAverage(self):
        total = 0
        for asignature in self.asignatures:
             total += asignature.getNote()
        return total/len(self.asignatures)
    def setAsig(self,asigName,asigNote):
        self.asigName = asigName
        self.asigNote = asigNote
        for asignature in self.asignatures:
             if asignature.getAsigName() == asigName:
                 return 'This asignature exist!'
        self.asignatures.append(Asignature(self.asigName,self.asigNote))

class App():
    def __init__(self,students):
        self.students = students
    def getData(self):
        for student in self.students:
            print(student.getName())
            print(student.getAge())
            print(len(student.asignatures))
            studentData = []
            for asignature in student.asignatures:
                studentData.append(asignature.getAsigName())
                studentData.append(asignature.getNote())
                studentData.append(asignature.asigState())
            print(*studentData)
            print(student.getAverage())
            
    


if __name__ == '__main__':
    asiges = [Asignature('Math',4),Asignature('Geography',3),Asignature('Chemestry',9)]
    student1= Student('Carlos',18,asiges)
    student2 = Student('Romero',21,asiges)
    student3 = Student('Pablo',80,asiges)
    students = [student1,student2,student3]
    aplication = App(students)
    aplication.getData()

             
        
        