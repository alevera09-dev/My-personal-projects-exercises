"""
Modulo con funciones de comprobacion de numeros pares e impares
"""

"""
Funciones necesarias:
* Comprobacion de si un numero es primo o no - completado
* Mostrar todos los numeros primos hasta el numero ingresado - completado
* Funcion de historial - completado
"""

#Crear funcion que tome un numero y compruebe si es primo o no
def is_prime(number:int) -> str:
    """Comprueba si un numero es primo o no.

    Args:
        number (int): El numero a comprobar.

    Returns:
        str: Pueden ser tres comprobantes:
    * "cero" si el numero es cero.
    * "primo" si el numero es primo.
    * "no primo" si el numero no es primo. 
    
    """
    
    main_primes = [2, 3, 5, 7]
    divisibles = 0

    if number == 0:
        return "cero"
    
    
    for i in main_primes:
        if number %i == 0:
            divisibles += 1
            
            
    if (divisibles < 1 or number in main_primes) and not number == 1:
        return "primo" 
            
    if divisibles > 0 or number == 1:
        return "no primo"
           
"""

Prueba =


numeros_no_primos = [
    1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 
    21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 
    35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 
    50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 
    64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 
    78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 
    92, 94, 95, 96, 98, 99, 100
]

for i in numeros_no_primos:
    print(is_prime(i))
    
Estado: Exitosa   
"""
#Crear una funcion que muestre todos los numeros primos hasta number
def all_primes(number:int) -> str:
    main_primes = [2, 3, 5, 7]
    divisibles = 0
    
    for i in range(2, number+1):
        divisibles = 0
        
        for j in main_primes:
            if i %j == 0:
                divisibles += 1
        
        if i in main_primes or divisibles < 1:
            print(i)

#Crear un funcion que guarde cada comprobacion en una lista como modo historial
historial_list = []
def historial(number:int=0, result:str=None, operation:str=None):
    if operation == "saved":
        historial_list.append(f"""Numero comprobado: {number}\n\tResultado: {result}""")
    if operation == "show":
        for i in range(len(historial_list)):
            print(f"{i+1}. {historial_list[i]}\n")

                               