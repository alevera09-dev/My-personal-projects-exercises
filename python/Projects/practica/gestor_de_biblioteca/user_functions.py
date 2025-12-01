from classes import Book, User, Biblioteca

biblioteca = Biblioteca()

def check_list_client(user_name):
    check_list_users: None = None
    
    for user in biblioteca.users:
        if user_name == user.name:
            check_list_users = "existente"
            break
    
    return check_list_users



def get_user(name):
    for user in biblioteca.users:
        if name == user.name:
            return user
        
        

def get_actual_user():
    global actual_user
    actual_user = ""
    
    while True:
        print("1. Ingresar.")
        print("2. Registrarse.")
        
        opc_user: str = input("\n>> ")
        
        if opc_user == "1":
            user_name: str = input("Tu nombre completo > ")
            
            check_user = check_list_client(user_name)
            
            if check_user == "existente":
                actual_user = get_user(user_name)
                print("\nIngreso correcto.\n")
                break
            
            else:
                print("Tu no existes en la lista de ususario de esta biblioteca, registrate!!")
            
        elif opc_user == "2":
            print("\nEsta bien, dame tus datos!!\n")
            
            user_name: str = input("Nombre: ")
            user_id: str = input("ID: ") 
            actual_user = User(user_name, user_id)   
            biblioteca.registar_usuario(actual_user)
            
        
                         
def menu_cliente():
    global opc_client
    
    print("\nMenu de cliente.")
    print(f"Usuario Actual: {actual_user.name}")
    
    print("1.Pedir prestado un libro.")
    print("2.Devolver libro.")
    print("3. Volver a menu principal.")
    
    opc_client = input("\n>> ")
    return opc_client



def obtener_libro(title):
    for book in biblioteca.books:
        if title == book.title:
            return book
    
   
    
def client_option_one():
    print("\nOkay que libro quieres, mejor que sepas el titulo.")
    
    title: str = input("Titulo del libro: ")
    
    search_book = biblioteca.buscar_libro(title)
    
    
    if search_book == "no existente":
        print("Este libro no lo tenemos.")
        
    else:
        state_book: Book = search_book.state
        
        if state_book == "prestado":
            print("El libro esta prestado")
            
        else:  
            book: Book = obtener_libro()
            book.prestado()
            actual_user.tomar_prestado(book)
            
            print("Tenemos el libro, lo agregaremos a tu lista de libros prestados, regrea al menu.")
    

        
def client_option_two():
    exist_book: bool
    
    print("\nOkey, que libros quieres devolver?\n")
    
    for book in actual_user.borrowed_books:
        print(f"\t{book.title}")

    print("Ingresa el titulo del libro", sep=" ")
    title_book: str = input(">> ")
    
    for book in actual_user.borrowed_books:
        if title_book == book.title:
            exist_book = True
            break
        
    if exist_book:
        book: Book = obtener_libro(title_book)
        actual_user.devolver(book)
        print("Todo bien")
            



