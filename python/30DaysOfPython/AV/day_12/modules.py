def random_user_id(char=6) -> str:
    """Genera una user_id aleatoria.

    Args:
        cha (int, optional): cantidad de caracteres del id generado. Defaults to 6.
                
    Returns:
        str: el id generado
    """   
    from random import choice
    from string import ascii_letters, digits
    
    #valid_characters -> lista de todas las letras y digitos validos en ASCII
    valid_characters = list(ascii_letters) + list(digits)    
    user_id = ""
    
    #generador aleatorio del user_id
    for i in range(char):
        user_id = user_id + choice(valid_characters)
    
    
    return user_id

def user_id_gen_by_user() -> str:
    """
    Basado en la funcion random_user_id().
    
    Puede generar mas de una user_id aleatoria.
    """    
    char = int(input("Número de caracteres[int]: "))
    number_of_ids = int(input("Cantidad de User_Id a generar[int]: "))
    
    for i in range(number_of_ids):
        print(random_user_id(char))
        
def rgb_color_gen():
    """Genera un codigo rgb aleatorio.

    Returns:
        str: El codigo rgb.
    """
    from random import randint
    
    rgb = []
    for i in range(3):
        rgb.append(randint(0,255))
    
    return f"rgb{rgb[0],rgb[1],rgb[2]}"        

def list_of_hexa_colors(cant:int) -> list:
    """Genera una lista de codigos hexadecimales aleatorios.

    Args:
        cant (int): Cantidad de codigo hexadecimal a generar.

    Returns:
        list: Lista con todos los codigos hexadecimales generados.
    """
    from string import digits
    from random import choice
    
    valid_characters = ["a","b","c","d","e","f"] + list(digits)
    hexa_code = "#"
    hexa_color = []
     
    for i in range(cant):
       for j in range(6):
            hexa_code = hexa_code + choice(valid_characters) 
        
        
       hexa_color.append(hexa_code)
       hexa_code = "#" 
       
    return hexa_color   
            
def list_of_rgb_colors(cant:int) -> list:
    """Toma un int como argumento y retorna una lista de rgb colors aleatoria.

    Args:
        cant (int): Cantidad de codigos rgb generados.

    Returns:
        list: Lista con los rgb generados.
    """   
    array_rgb_colors = []
    for i in range(cant):
        array_rgb_colors.append(rgb_color_gen())
    
    return array_rgb_colors    
            
def generate_colors(opc:str, cant:int) -> list:
    """Genera una lista de codigo/s rgb o hexadecimales dependiendo del valor dado al argumento _opc_.

    Args:
        opc (str): Tipo de codigo/s que se desea generar y retornar.
        
            Hay dos tipos de opc:
                * "hexa": Generar codigo hexadecimal. 
                * "rgb": Generar codigo rgb.
        
        
        cant (int): Cantidad de codigos que tendra la lista retornada.

    Returns:
        list: Lista con el/los codigo/s elegido/s.
    """
    valid_opc = ("rgb", "hexa")
    
    if opc not in valid_opc:
        return "Opc invalida"
    if opc == valid_opc[0]:
        return list_of_rgb_colors(cant)
    if opc == valid_opc[1]:
        return list_of_hexa_colors(cant)

def shuffled_list(array:list) -> list:
    """Toma un argumento tipo list y devuelve una lista barajada.

    Args:
        array (list): Any list.

    Returns:
        list: Lista con los mismo elementos pero barajada osea reorganizada aleatoriamente.
    """
    from random import shuffle
    shuffle(array)
    return array

def gen_matrix():
    """
    Genera y devuelve una lista de siete números enteros únicos
    en un rango de 0 a 9.
    """
    import random
    return random.sample(range(10), 7)


print(generate_colors("hexa", 10))