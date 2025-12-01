"""
Back-end de notepy:
    Funcionalidades:
        *Agregar estudiante:
                            Nombre
                            Matricula
                            
        *Registrar notas de diferentes asignaturas
        *Calcular promedio de notas de cada estudiante
        *Listar estudiantes con sus notas
        *Permitir editar y eliminar notas o estudiantes
        *Generar reportes con estudiantes que aprueban o reprueban.
        *Guardar y cargar los datos desde archivos para persistencia.
        *Soportar múltiples cursos o grupos.
        
"""
import json


#Base de datos de los estudiantes, cada key es un estudiante y su valor sera una lista con sus datos(dni, notas, etc)
bd_students = {}


#Listado de estudiantes pra una busqueda rapida
student_list = []

#Archivo de guardado externo de la base de datos
save_file = "bs_students_external.json"


#Crear funcion que agregue estudiantes a local_bd_students
def add_student(name:str, dni:int):
    #agrega al estudiante en local_bd_students con el formato correspondiente
    name = name.replace(" ", "_")
    name_list = name.split("_")
    
    if len(name_list) == 2:
        names = name_list[0]
        surnames = name_list[1]
    if len(name_list) == 3:
        names = name_list[0]
        surnames = name_list[1] + " " + name_list[2]
    if len(name_list) == 4:
        names = name_list[0] + " " + name_list[1]
        surnames = name_list[2] + " " + name_list[3]
            
    bd_students[name.lower()] = {"names": names, "surnames": surnames, "dni": dni, "grades":{}}


#Crear una funcion que calcule el gpa de todos los estudiantes registrados 
def gpa(grades_list:list):
    return sum(grades_list) / len(grades_list)


#Crear funcion que registre notas de diferentes materias a un estudiante ya agregado a la base de datos
def register_notes(grade:float, subject:str, name_student:str):    
    #El estudiante existe?
    name_student = name_student.lower()
    name_student = name_student.replace(" ", "_")
    coincidencias = 0
    grades_list = []
    
    for name in bd_students:
        if name_student == name:
            coincidencias += 1
        
        
    if coincidencias > 0:
        grades = {subject.lower(): grade}
        grades_list.append(grade)
        grade_points_average = {"gpa": gpa(grades_list)}
        grades.update(grade_points_average)       
        bd_students[name_student]["grades"].update(grades) 
        
    else:
        return "estudiante no existente"        
    

#Crear funcion que liste todos los estudiantes
def to_list_students():
    for name in bd_students:
        name = name.replace(" ", "_")
        name = name.lower()
        student_list.append(name)


#Crear funcion que permita editar al maestro a un estudiante, sus notas o borrarlo
def edit_student(option:str, name_student:str,
                 new_grade:float=0, subject:str=None):
    
    name_student = name_student.lower
    name_student = name_student.replace(" ", "_")
    
    if name_student not in student_list:
        return "estudiante no existente"
    
    if subject not in bd_students[name_student]["grades"]:
        return "materia no existente"
    
    
    if option == "edit_grades":
        bd_students[name_student][subject.lower()] = new_grade
        return "exito"
    
    if option == "delete_grades":
        bd_students[name_student].pop(subject)
        return "exito"
    
    if option == "delete_student":
        bd_students.pop(name_student)
        return "exito"        
   
   
#Crear funcion que genere reportes con estudiantes que aprueben o reprueben
def report_course():
    print("\nReporte de curso:\n")
    print("Estudiantes aprobados:\n")
    
    for student in bd_students:
        if bd_students[student]["grades"]["gpa"] >= 7.0:
            print(f"""\t{student.capitalize()}: {bd_students[student]["grades"]["gpa"]}""")
            
    print("\nEstudiantes reprobados:\n")
    
    for student in bd_students:
        if bd_students[student]["grades"]["gpa"] < 7.0:
            print(f"""\t{student.capitalize()}: {bd_students[student]["grades"]["gpa"]}""")
    


#Crear funcion que guarde los datos en un .json
def save_data():
    
    with open(save_file, "w") as save:
        json.dump(bd_students, save, indent = 4)


#Crear funcion que cargue los datos del archivo .json
def load_data():

    with open(save_file, "r") as load:
        bd_students = json.load(load)
    
    return bd_students    


#Despues de todo hacer un soprote para multiples cursos o grupos. 




    