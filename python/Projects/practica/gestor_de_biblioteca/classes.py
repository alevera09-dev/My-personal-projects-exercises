#Classes para gestor de biblioteca

class Book(object):
    def __init__(self, title:str, autor:str, isbn:str):
        self.title = title
        self.autor = autor
        self.isbn = isbn
        self.state = "disponible"
    
    def __str__(self):
        self.reference_book: str = f"""Title Book: {self.title}
Autor Book: {self.autor}
ISBN Book: {self.isbn}
State Book: {self.state}"""
        
        return self.reference_book
                                          
    def prestado(self):
        if self.state == "disponible":
            self.state = "prestado"
        else:
            print("El libro esta prestado")
        
    def devuelto(self):
        if self.state == "prestado":
            self.state = "disponible"        
        else:
            print("El libro ya esta en la biblioteca")
            
            
               
    
class User(object):
    def __init__(self, name:str, id:str):
        self.name = name
        self.id = id
        self.borrowed_books = []
        
    def __str__(self):
        self.user_reference: str = f"""Hola soy {self.name}"""    
        return self.user_reference
        
        
        
    def tomar_prestado(self, book):
        self._borrowed_books.append(book)
    
    def devolver(self, book):
        self._borrowed_books.remove(book)
    
        

class Biblioteca(object):
    def __init__(self):
        self.users = []
        self.books = []
    
    def registar_usuario(self, name_user:str):
        self.users.append(name_user)
        
    def registar_libro(self, book:Book):
        self.books.append(book)
        
    def eliminar_libro(self, title_book:str):
        self.books.remove(title_book)    
    
    def buscar_libro(self, title_book:str):
        book_searched: Book
        
        for book in self.books:
           if  title_book == book.title:
               book_searched = book
               break
           
        if book_searched != None:
            return book_searched
        else:
           return "no existente"
         

"""
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


biblioteca = Biblioteca()

for libro in libros:
    new_book = Book(libro[0], libro[1], libro[2])
    biblioteca.registar_libro(new_book)
"""

        