"""
NotePy una aplicacion que permita a profesores gestionar las notas de sus estudiantes

main.py = front-end
notepy.py = back-end

front-end:
    1.Opciones:
        * Agregar estudiantes con nombre y matricula
        * Registrar notas para diferentes asignaturas
        * Editar notas o estudiantes
        * 
        
"""
import notepy


def main_options():
    print("1. Agregar estudiante.")
    print("2. Registrar notas academicas.")
    print("3. Editar base de datos.")
    print("4. Generar reporte de clase/grupo")
    print("5. Salir.")
    
    
def handle_option_1():
    print("\nHas elegido agregar un estudiante.\n")
    
    new_student_name = input("Nombre completo del nuevo estudiante >> ")
    new_student_dni = int(input("DNI del nuevo estudiante >> "))
    
    notepy.add_student(new_student_name, new_student_dni)
    
    print(f"\nEstudiante {new_student_name} a sido agregado exitosamente.\n")
    notepy.to_list_students()

    
    
def handle_option_2():
    stop_1 = False
  
    
    print("\nHas elegido registrar notas academicas.")
    print("Nota: Ten en cuenta que el estudiante necesita estar agregado con anterioridad.\n")
    
    print("Estudiantes en base de datos:")
    for student in notepy.student_list:
        print("\t", student)
        
    while True:
        if stop_1:
            break
        
        student = input("\nElige el estudiante a registrar notas >> ")
        new_subject = input("Elige la materia de la nota que registraras >> ")
        new_grade = float(input(f"Ingresa la nota de {new_subject} >> "))
        
        notepy.register_notes(new_grade, new_subject, student)
        notepy.save_data()
        
        print("\nRegistro exitoso!!")
        
        while True:
            
            register_opc = input("Quieres registrar mas notas? si o no\n")
            
            match register_opc:
                case "si":
                    stop_1 = False
                    break
                    
                case "no":
                    stop_1 = True
                    break
                    
                case _:
                    print("Opcion inexistente, vuelve a intentarlo.")
                    

def handle_option_3():
    stop_1 = False
    stop_2 = False
    stop_3 = False
    
    print("Has elegido editar la base de datos.\n")
    
    while True:
        if stop_1:
            break
        
        print("1. Editar Nota")
        print("2. Eliminar Nota(junto a asignatura)")
        print("3. Eliminar estudiante")
        
        while True:
            if stop_2:
                break
            
            while True:
                if stop_3:
                    break
                
                edit_option = input()
                
                
                if edit_option in ["1", "2", "3"]:
                    
                    if edit_option == "1":
                        student = input("\nIngrese el nombre del estudiante a editar >> ")
                        subject = input("Ingrese la materia a editar >> ")
                        new_grade = input(f"Ingrese la nueva nota de {subject} >> ")
                        
                        resultado_de_la_edicion = notepy.edit_student("edit_grades", student, new_grade, subject)
                        
                        if resultado_de_la_edicion == "estudiante no existente":
                            print("\nEL estudiante no existe.")
                        
                        elif resultado_de_la_edicion == "materia no existente":
                            print("\nMateria no existente")
                        
                        else:
                            print("\nEdicion exitosa.")    
                    
                    
                    elif edit_option == "2":
                        student = input("Ingrese el estudiante a editar >> ")
                        subject = input("Ingrese la materia a eliminar >> ")
                        
                        resultado_de_la_edicion = notepy.edit_student("delete_grade", student, subject=subject)
                        
                        
                        if resultado_de_la_edicion == "estudiante no existente":
                            print("\nEstudiante inexistente.")
                            
                        elif resultado_de_la_edicion == "materia no existente":
                            print("Materia inexistente.")
                            
                        else:
                            print("Edicion exitosa.")
                            
                    elif edit_option == "3":
                        student = input("\nIngresa al estudiante a eliminar.")
                        
                        resultado_de_la_edicion = notepy.edit_student("delete_student", student)
                        
                        
                        if resultado_de_la_edicion == "estudiante no existente":
                            print("Estudiante inexistente.")
                        
                        elif resultado_de_la_edicion == "materia no existente":
                            print("\nMateria inexistente.")
                        
                        else:
                            print("\nEliminacion exitosa.")        
                
                    notepy.save_data()
                    stop_3 = True
                    
                    
                else:
                    print("Opcion inexistente, vuelve a intentarlo")
                    stop_3 = False    
            
            
            
            print("\n Quieres editar a otro estudiante? si o no.")
            
            while True:
                
                edit_option_2 = input(">> ")
                
                match edit_option_2:
                    case "s":
                        break
                    
                    case "n":
                        stop_1 = True
                        stop_2 = True
                        break
                    
                    case _:
                        print("Opcion inexistente, vuelve a intentarlo.")


def handle_option_4():
    print("\nHas elegido generar reporte de grupo.\n")
    
    notepy.report_course()



            
            
def main_menu():
    stop = False
    
    print("\n|NotePy|")
    print("\nDesarrollador: Alejandro Vera.\n")
    
    while True:
        notepy.save_data()
        notepy.load_data()
        
        if stop:
            break
        
        main_options()
        
        
        while True:
            main_opc = input("\n>> ")
            
            match main_opc:
                case "1":
                    handle_option_1()
                    stop = False
                    break
                
                case "2":
                    handle_option_2()
                    stop = False
                    break
                
                case "3":
                    handle_option_3()
                    stop = False
                    break
                    
                case "4":
                    handle_option_4()
                    stop = False
                    break
                    
                case "5":
                    print("\nGracias por usar el programa, saliendo...")
                    stop = True
                    break
                
                case _:
                    print("Opcion no existente, intentalo de nuevo.")
            
            
            
            
            
if __name__ == "__main__":
    main_menu()