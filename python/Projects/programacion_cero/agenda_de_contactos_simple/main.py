"""
Agenda de contactos simples desarrollado por mi en python.

* main.py = script con ejecucion principal que mostrara el menu de usuario.
* contacts_functions.py = modulo con la logica del programa.

"""
import contacts_functions as functions

"""
Menu de usuario
"""

#El titulo y opciones
def title_options():
    print("\n")
    print("="*14)
    print("| PyContacts |")
    print("="*14)
    print("\n1.Añadir contactos.")
    print("2.Listar contactos.")
    print("3.Buscar contactos.")
    print("4.Editar contactos.")
    print("5.Eliminar contactos.")
    print("x. Exit.")


"""
Opciones
"""

#Opcion 1
def handle_option_1():
    terminar_bucle = False
    print("\n¡Has elegido añadir contactos!\n")
    
    while True:
        #Si se elige volver al menu el bucle termina
        if terminar_bucle:
            break
        
        #Nombre del contacto
        name_contact = input("Ingresa el nombre que tendra el nuevo contacto -> ")      
        
        #Número telefonico
        phone_number = input(f"Ingresa el numero telefonico de {name_contact} -> ")
        
        #Correo electronico
        adress_email = input(f"Ingresa el correo electronico de {name_contact} -> ")
        
        #Añadir el contacto
        functions.add_contact(name_contact, phone_number, adress_email)
        
        #Si es exitoso sale su mensaje
        print("\nContacto creado con exito")
        
        print("\nQuieres crear otro contacto o volver al menu principal?")
        print("\n1.Crear otro contacto.")
        print("q.Volver al menú principal.")
        opc_1 = input(">> ")
        
        opcion_valida = False
        while True:
            if opcion_valida:
                break
            
            match opc_1.lower():
                case "1":
                    opcion_valida = True
                    terminar_bucle = False
                case "q":
                    opcion_valida = True
                    terminar_bucle = True
                case _:        
                    print("\nOpción inexistente, intentalo de nuevo.")
                    opc_1 = input(">> ")

def handle_option_2():
    print("¡Has elegido la opcion de listar contactos!")
    
    name_new_list = input("Ingresa un nombre para la nueva lista -> ")
    
    print("\nLista de todos los contactos:")
    functions.show_contacts()
    
    new_contact = input("Elige un contacto al que quieras listar en la nueva lista(Ingresa el nombre) -> ")
    
    functions.to_list(name_new_list=name_new_list, contact=new_contact)
    
    
    
    
    
    
    


#Menu principal
def main_menu():
    while True:
        title_options()
    
        main_opc = input("\nQue quieres hacer? -> ")
    
        if main_opc == "1":
            handle_option_1()
        if main_opc == "2":
            handle_option_2()    





if __name__ == "__main__":
    print(functions.contacts)