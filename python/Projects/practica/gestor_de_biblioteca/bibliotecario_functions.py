from classes import *

biblioteca = Biblioteca()

def menu_bibliotecario():
   
    print("\nMenu Bibliotecario\n")
    
    print("1.Registrar Libro.")     
    print("2.Eliminar Libro.")
    print("3.Lista de Libros")
    print("4.Volver al menu principal.")
    
    opc_bibliotecario: str = input(">> ")
    return opc_bibliotecario 




def bibliotecario_option_one():
    print("\nElegiste registar libro, dame el titulo.\n")
    
    title_book: str = input(">> ")
    
    biblioteca.registar_libro(title_book)
    
    print("Listo!!!")

def bibliotecario_option_three():
    print("\nLISTA DE LIBROS:\n")
    for book in biblioteca.books:
        print(book, "\n") 


def bibliotecario_option_two():
    while True:
        print("\n\Elegiste eliminar un libro, dame el titulo de ese libro.")
    
    
        title_book: str = input(">> ")
    
        try:
            biblioteca.eliminar_libro(title_book)
            print("Listoo!!")
            break
        except ValueError:
            print("El libro no existe, instentalo de nuevo.")
            