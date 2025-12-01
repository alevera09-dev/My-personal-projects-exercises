from cryptography.fernet import Fernet
"""
Funcionalidades para validador de contraseñas

Funciones:

* Validador de contraseña - Completado
    Reglas: * 8 caracteres minimo
            * 1 letra mayuscula, numero y caracter especial 
* Retroalimentacion al ususario: porque la contraseña no es valida? - completado  
* Guardar contraseñas validas en archivos cifrados - completado          
"""


#Crear una funcion que tome una contraseña y verifique si es valida con las reglas de arriba
def check_password(password:str) -> str:
    """Validador de contraseña.

    Args:
        password (str): La contraseña a comprobar.

    Returns:
        str: retorna si la contraseña es valida o no valida
    """
    import string
    digits = list(string.digits)
    caracter_special = list(string.punctuation)
    mayus = list(string.ascii_uppercase)
    digits_in_password = 0
    special_in_password = 0
    mayus_in_password = 0
    return_list = ["", """"""]  #[valides, retroalimentacion]
    
    if len(password) < 8:
        return_list[0] = "no valida" 
        return_list[1] = "La contraseña debe ser de al menos 8 caracteres"
        return return_list
    
    for digit in digits:
        if digit in password:
            digits_in_password += 1 
    for special in caracter_special:
        if special in password:
            special_in_password += 1
    for letter in mayus:
        if letter in password:
            mayus_in_password += 1
            
    if digits_in_password < 1:
        return_list[1] = """* La contraseña debe tener minimo 1 numero(1234...)"""
    if special_in_password < 1:
        return_list[1] = return_list[1] + """\n* La contraseña debe tener minimo un caracter especial(@#$%...)"""
    if mayus_in_password < 1:
        return_list[1] = return_list[1] + """\n* La contraseña debe tener minimo una letra mayuscula(ABCD...)"""

    if digits_in_password and special_in_password and mayus_in_password >= 1:
        return_list[0] = "valida"
        return return_list
    else:
        return_list[0] = "no valida"
        return return_list

"""
Pruebas
valid = check_password("alejandrovera")                        
print(f"{valid[0]}\n\nRetroalimentacion: \n{valid[1]}")

Estado de prueba: exitosa.
"""




#Crear una funcion que cree una key 
def generate_key():
    new_key = Fernet.generate_key()
    
    with open("key_saved.bin", "wb") as file:
        file.write(new_key)
#Crear funcion que carge la key guardada       
def load_key():
    
    with open("key_saved.bin", "rb") as load:
        key = load.read()
    return key

#Crear una funcion que la contraseña encriptada en binario
def save_password(password:str):
    key = load_key()
    cifrar = Fernet(key)   
    password_encrypt = cifrar.encrypt(password.encode())
    
    with open("passwords_saved.enc", "wb") as saved:
        saved.write(password_encrypt)
    



#Crear una funcion que carge las contraseñas
def load_password():
    key = load_key()
    descifrar = Fernet(key)
    
    with open("passwords_saved.enc", "rb") as password_load:
        password = password_load.read()
    
    password_decrypt = descifrar.decrypt(password).decode()
    return password_decrypt


"""
Pruebas
save_password("210109@Vl")
print(load_password())

Estado de prueba: Exitosa
"""    
    
    
    



