#Archivo principal de la biblioteca
import sys, user_functions, bibliotecario_functions
from classes import *

biblioteca = Biblioteca()


def cargar_libros():
    libros = [
        ["Cien años de soledad", "Gabriel García Márquez", "978-0307474728"],
        ["1984", "George Orwell", "978-0451524935"],
        ["Orgullo y prejuicio", "Jane Austen", "978-0486284736"],
        ["Un mundo feliz", "Aldous Huxley", "978-0060850524"],
        ["El Gran Gatsby", "F. Scott Fitzgerald", "978-0486474267"],
        ["Don Quijote de la Mancha", "Miguel de Cervantes", "978-8424115160"],
        ["Matar a un ruiseñor", "Harper Lee", "978-0446310789"],
        ["El Hobbit", "J.R.R. Tolkien", "978-0547928227"],
        ["Crimen y castigo", "Fyodor Dostoevsky", "978-0486415873"],
        ["Frankenstein", "Mary Shelley", "978-0486282114"]
    ]




    for libro in libros:
        new_book = Book(libro[0], libro[1], libro[2])
        biblioteca.registar_libro(new_book)



def title_app():
    print("\nBiblioteca de Alex.\n")
    
    
    
def type_user_func():
    global type_user
    type_user = ""
    
    password: str = "12345"
    
    print("Eres un Cliente o El Bibliotecario?\n")
    
    print("1. Cliente.")
    print("2. Bibliotecario.")
    print("3. Salir")
    
    opc_user = input("\nQue eres? >> ")
    
    while True:
        if opc_user == "1":
            print("\nElegiste cliente.\n")
            print("\n")
            type_user = "user"
            break
        
        elif opc_user == "2":
            print("\nElegiste bibliotecario.\n")
            check_password: str = input("Entonces digita la contraseña de la biblioteca: ")
            
            if check_password == password:
                print("\nCorrecto.\n")
                type_user = "bibliotecario"
                break
                
            else:
                print("\nMentiroso!!")
                sys.exit()
        
        
        elif opc_user == "3":
             sys.exit()
                     
        else:
            print("\nNo se que elegiste ciego, vuelve a intentarlo.\n")
            
        
 
 
def main_menu():
    veces: int = 0
    while True:
        title_app()
        type_user_func()
        
        if type_user == "bibliotecario":
            while True:
            
                opc_bibliotecario = bibliotecario_functions.menu_bibliotecario()   
                
                if opc_bibliotecario == "1":
                    bibliotecario_functions.bibliotecario_option_one()
                if opc_bibliotecario == "2":
                    bibliotecario_functions.bibliotecario_option_two()
                if opc_bibliotecario == "3":
                    bibliotecario_functions.bibliotecario_option_three()    
                if opc_bibliotecario == "4":
                    break
                else:
                    print("opcion no existente, vuelve a intentarlo.")
        
        if type_user == "user":
            
            
            while True:
                if veces < 1:
                    user_functions.get_actual_user()
                
                user_functions.menu_cliente()
                                
                if user_functions.opc_client == "1":
                    user_functions.client_option_one()
                elif user_functions.opc_client == "2":
                    user_functions.client_option_two()
                elif user_functions.opc_client == "3":
                    break
                else:
                    print("Opcion no existente, vuelve a intentarlo.")    
            
                veces += 1


if __name__ == "__main__":
    cargar_libros()
    main_menu()
        