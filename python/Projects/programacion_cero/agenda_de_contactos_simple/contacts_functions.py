"""
Estructura de contactos:
                           contacts = {
                               name_contact : [phone,
                                               mail ]
                           } 


Estructura de listas personalizadas:
                                        customs_list = {
                                            name_custom_list : [name_contact 1
                                                                name_contact 2
                                                                name_contact n]
                                        }
"""
#Guardado de datos
contacts = {}   #Donde se guardan todos los contactos y sus datos
customs_list = {}   #Lista creadas por los usuarios




#Funciones secundarias:
def show_contacts():
    for i in contacts:
        name_contact:str = i.replace("_", " ")
        name_contact = name_contact.capitalize() 
        print(f"Contacto: {name_contact}")
        for j in range(len(contacts[i])):
            if j == 0:
                print(f"\tNúmero Telefonico: {contacts[i][j]}")
            if j == 1:
                print(f"\tCorreo Electronico: {contacts[i][j]}\n")    



#Funciones de comprobacion de datos:
def check_mail(email:str) -> bool:
    """Validador basico de e-mails. 

    Args:
        email (str): Toma e-mail para evaluarlo.

    Returns:
        bool: Si es False el e-mail es invalido, si es True es valido.
    """
    from string import punctuation
    characters_invalids = list(punctuation)
    characters_invalids.remove(".")
    errors = 0
    
    #Validacion de e-mail
    if "@" not in email or " " in email:
        return False
    
    prefijo_dominio = email.split("@")
    
    for i in characters_invalids:
        if i in prefijo_dominio[0] or i in prefijo_dominio[1]:
            errors += 1
    
    if errors > 0 or prefijo_dominio[0][-1] == "." or prefijo_dominio[0][0] == "." or prefijo_dominio[1][0] == "." or prefijo_dominio[1][-1] == ".":
        return False
    
    if True:
        return True    
def check_phone(phone:str) -> bool:
    """Toma un numero telefonico y evalua si es valido o no(solo Colombia).

    Args:
        phone (str): Número de telefono. 

    Returns:
        bool: Si es falso es invalido, si es True es valido.
    """
    #Arreglar phone para hacerlo legible   
    phone = phone.replace(" ", "")
    
    if " " in phone:
        return False
    
    if len(phone) > 10:
        return False
    
    try:
        phone = int(phone)
    except ValueError:
        return False
    else:
        return True
def check_name(name:str, data_structure:dict) -> bool:
    coincidencias = 0
    
    if len(data_structure) < 1:
        return True
    
    
    for i in contacts:
        if name == i:
            coincidencias += 1
            break
    if coincidencias > 0:
        return False
    if True:
        return True




#Guardado y cargado de datos
def save_load(operation:str, arch_save:str="contacts_saved", new_list:list=[]):
    """_summary_

    Args:
        operation (str): Operacion que hara la funcion.
        
            Tipos de operaciones:    
                * "save": Guarda los contactos a un archivo .json.
                * "load": Carga esos contactos del archivo .json.

    Returns:
        type: solo cuando carga retorna el diccionario contactos cargado con datos guardados anteriormente.
    """
    import json
    import os
    
    
    
    #Codigo para comprobar si el directorio correspondiente a los archivos del programa existen.
    
    nombre_directorio = "saves_archives"    #nombre del directorio que debe existir.
    nombre_archivo_guardado = arch_save + ".json"     #nombre del archivo donde se deben guardar los contactos.
    
    ruta_completa = os.path.join(nombre_directorio, nombre_archivo_guardado)    #Ruta completa donde debe estar el archivo.
    
    #si el directorio no existe se crea.
    os.makedirs(nombre_directorio, exist_ok=True)
    
    if arch_save == "contacts_saved":
        folder_contacts = contacts
    else:
        folder_contacts = customs_list         
    
    #Ahora guarda o carga datos dependiendo de operation=
    if operation == "save":    
        with open(ruta_completa, "w") as save:
            json.dump(folder_contacts, save, indent=4)
            
    if operation == "load":
        with open(ruta_completa, "r") as load:
            dict_load:dict = json.load(load)
        return dict_load    



#Los datos guardados
contacts = save_load("load")
customs_list = save_load("load")



#Funciones principales:
def add_contact(name:str, number_phone:str, email_adress:str):
    """Crea y añade un nuevo contacto.

    Args:
        name (str): Nombre del contacto.
        phone (str): Número telefonico del contacto.
        email (str): correo eletronico del contacto.
    """
    
    #Arreglar el nombre y nuemro telefonico para hacerlo mas legible
    name = name.lower()
    name = name.replace(" ", "_")
    number_phone = number_phone.replace(" ", "")
    
    #Evaluar los datos y volver a pedirlos si son invalidos
    name_valid = check_name(name=name, data_structure=contacts)
    phone_valid = check_phone(phone=number_phone)
    
    #Evaluar el nombre
    while not name_valid:
        name = input("Este nombre ya lo tiene un contacto guardado, elige uno diferente -> ")
        name = name.lower()
        name = name.replace(" ", "_")
        name_valid = check_name(name)
        
    while not phone_valid:
        number_phone = input("Numero invalido, el formato valido es XXX XXX XX XX -> ")
        phone_valid = check_phone(phone=number_phone)
        
    #Evaluar el correo electronico
    email_valid = check_mail(email=email_adress)
    while not email_valid:
        email_adress = input("Correo electronico invalido, el formato es: prefijo@dominio.com/org/etc -> ")    
        email_valid = check_mail(email=email_adress)
    
     
    #Agregar contacto a contacts   
    contacts[name] = [number_phone, email_adress]
    
    #Guardar contactos externamente
    save_load("save")
    
    
def to_list(name_new_list:str, contact):
    #Arreglar el nombre de la nueva lista y el nombre del contacto
    name_new_list = name_new_list.replace(" ", "_")
    name_new_list = name_new_list.lower()
    contact = contact.replace(" ", "_")
    contact = contact.lower()
    
    valid_name = check_name(name_new_list, customs_list)
    while not valid_name:
        name_new_list = input("Ya existe una lista con ese nombre, elige otro -> ")
        name_new_list = name_new_list.replace(" ", "_")
        name_new_list = name_new_list.lower()
        valid_name = check_name(name_new_list, customs_list)

    valid_contact = contact in contacts
    while not valid_contact:
        print("El contacto elegido no existe, elige un contacto existente")
        contact = input(">> ")
        valid_contact = contact in contacts
        
    customs_list[name_new_list] = [contact]
    
    save_load("save", arch_save=customs_list)    
    
    
    
    
    
    pass

def contact_search(name_contact:str):
    pass

def contact_edit(name_contact:str, phone:str, mail:str):
    pass

def delete_contact(name_contact:str):
    pass


