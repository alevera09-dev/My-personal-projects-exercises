import functions
from termcolor import colored


#front-end
while True:
    #Menu de opciones
    
    """
       * resumen mensual
       
       * editar registros
            * editar valor del ingreso/gasto
            * editar categoria
            * editar fecha
            * eliminar
            * input() para eleccion entre las subopciones de editar registros
            
    
    
    """
    
    #Titulo
    print(colored("\n>> Administrador de finanzas <<", (255,222,33), "on_black", ["bold"]))
    
    
    #Opciones
    print(colored("\n1 > Nuevo Registro.", (255, 222,33)))
    print(colored("2 > Resumen Mensual.", (255, 222, 33)))
    print(colored("3 > Editar Registros.", (255, 222, 33)))
    print(colored("4 > Salir.", (255, 233, 33)))

    opc = input(colored("\nOpción número > ", (255, 233, 33)))
    
    #logica de opciones
    match opc:
        case "1":
            functions.new_register()
        
        case "2":
            functions.finance_summary()
        
        case "3":
            functions.finance_edit()        
        case "4":
            print(colored("\nGracias por usar este programa", (255, 233, 33)))
            print(colored("Saliendo del programa...", (255, 233, 33)))
            break
        
        case _:
            print(colored("\nOpcion invalida, intenta elegir una de las opciones del menú", (255, 233, 33)))               