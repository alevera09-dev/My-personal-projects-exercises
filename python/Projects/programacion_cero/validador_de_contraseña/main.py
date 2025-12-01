"""
Aplicacion que valida la seguridad de contraseñas segun algunas reglas
"""
"""
Lo necesario:
* Menu principal:

    * Titulo - completado
    * programa principal - completado
    * 
"""
import password_functions as psfn

def main_menu():
    #Hacer titulo
    print("\n|***_Validador de contraseñas en python_***|")
    print("Developer: Alejandro Vera.\n")
    
    while True:
        #Hacer diseño para la funcion check_password
        print("Ingresa una contraseña a comprobar")
        input_password = input(">> ")
        
        valid = psfn.check_password(input_password)
        
        print(f"La contraseña {input_password} es {valid[0]}")
        
        if valid[0] == "valida":
            print("\nQuieres guardar esta contraseña?\n")
            opc = input("s/n >> ")
            
            match opc:
                case "s":
                    psfn.save_password(input_password)
                    print("Guardado exitoso.")
                    break
                case "n":
                    break   
                case _:
                    print("\nRespuesta no valida, saliendo...")
                    break    
                
                
        if valid[0] == "no valida":
            print(f"Fallos:{valid[1]}")
            
        
        
if __name__ == "__main__":
    main_menu()            