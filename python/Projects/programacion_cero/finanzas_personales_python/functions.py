from termcolor import colored

#BACK_END

#Diccionarios de los registros
income_records = {
    
}

expense_records = {
    
}

categories = ("Publico", "Corporativo", "Personal")


#Mini-Funciones
def record_type()->str:
    """Hace elegir entre los dos tipos de registro.

    Returns:
        str: El tipo de registro elegido.
    """
    print(colored("\nElige un tipo de registro", (255,233,33)))
    print(colored("1. > De ingreso", (255, 233, 33)))
    print(colored("2. > De gasto", (255, 233, 33)))
    
    type_opc = input(colored("\nOpción numero", (255, 233, 33)))
    
    while type_opc not in ["1","2"]:
        type_opc = input(colored("\nOpción numero", (255, 233, 33)))
    
    if type_opc == "1":
        return "ingreso"
    if type_opc == "2":
        return "gasto"
def check_date(date:list) -> bool:
    """Toma una fecha descomprimida en lista con formato[dd, mm, aaaa] y retorna un Bool dependiendo de si la fecha es valida o no.

    Args:
        date (list): Lista de fecha descomprimida con formato [dd, mm, aaaa].

    Returns:
        bool: True si la fecha es correcta y False si es incorrecta
    """
    if int(date[0]) < 1 or int(date[0]) > 31 or int(date[1]) < 1 or int(date[1]) > 12 or int(date[2]) < 2000:
        return False
    if int(date[1]) == 2 and int(date[0]) not in range(1,28):
        return False
    if (int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11) and int(date[0]) > 30:
        return False
    if True:
        return True    
def check_months()-> dict:
    """Cuando es llamada ordena todos los registros en fechas diferentes de mes_año.

    Returns:
        dict: El dictionary con llaves equivalente a las fechas(mes_año) y su valores siendo las id de cada registro.
    """
    
    date_records = {}
    if len(income_records) > 0:
        for i in income_records:
            income_date = income_records[i][2][1] + "_" + income_records[i][2][2]
        
            if income_date not in date_records:
                date_records[income_date] = [i]
            else:
                date_records[income_date].append(i)
            
    if len(expense_records) > 0:        
        for i in expense_records:
            expense_date = expense_records[i][2][1] + "_" + expense_records[i][2][2]
        
            if expense_date not in date_records:
                date_records[expense_date] = [i]
            else:
                date_records[expense_date].append(i)

    return date_records
def funcion_ingresos_brutos(date_records:dict, opc_date:str) -> float:
    """Calcula y retorna los ingresos brutos de los registros tipo income.

    Args:
        date_records (dict): Tiene que ser el dictionary date_records.
        opc_date (str): Tiene que ser la variable opc_date.

    Returns:
        float: Los ingresos brutos.
    """
    ingresos_brutos = 0
    
    #Obtener los ingresos brutos totales
    for i in date_records[opc_date]:
        try:
            ingresos_brutos += income_records[i][0] 
        except KeyError:
            continue
    
    return ingresos_brutos
def funcion_gastos_brutos(date_records:dict, opc_date:str) -> float:
    """Calcula y retorna los gastos brutos de los registros tipo expense.

    Args:
        date_records (dict): Tiene que ser el dictionary date_records.
        opc_date (str): Tiene que ser la variable opc_date.

    Returns:
        float: Los gastos brutos.
    """
    gastos_brutos = 0
    
    #Obtener los gastos brutos totales
    for i in date_records[opc_date]:
        try:
            gastos_brutos += expense_records[i][0] 
        except KeyError:
            continue
    return gastos_brutos        
def edit_record(type_record:str):
    if type_record == "ingreso" or type_record == "gasto" and len(income_records) < 0:
        print(colored("\nNo hay registros", (255, 233, 33)), "\n")
        
    if type_record == "ingreso":
        print(colored("\n>> Registros de ingresos <<", (255, 233, 33)), "\n")
        for i in income_records:
            print(colored(i, (255, 233, 33)))
                
        edit_record = input(colored("Ingresa la id de el registro que quieras editar > ", (255, 233, 33)))
        
        while edit_record not in income_records:
            print("\n", colored("Id inexistente, vuelve a intentarlo.", (255, 233, 33)))
            edit_record = input(colored("Ingresa la id de el registro que quieras editar > ", (255, 233, 33)))
               
    if type_record == "gasto":
        print(colored("\n>> Registros de gastos <<", (255, 233, 33)), "\n")
        for i in expense_records:
            print(colored(i, (255, 233, 33)))
            
        edit_record = input(colored("Ingresa la id de el registro que quieras editar > ", (255, 233, 33)))
        
        while edit_record not in income_records:
            print(colored("\nId inexistente, vuelve a intentarlo.", (255, 233, 33)))
            edit_record = input(colored("Ingresa la id de el registro que quieras editar > ", (255, 233, 33)))
    
    return edit_record        



#Funciones principales
def new_register():
    """Funcion que agrega nuevos registros.
    """   
    #Verificar que tipo de registro es
    type_record = record_type()
    
    
    #Pedir valor del registro
    while True:
        try:
            value = float(input(colored(f"\nIngrese el valor del {type_record} > ", (255, 233, 33))))
        except ValueError:
            print(colored("\nValor incorrecto, intentelo de nuevo y ingrese un número.", (244, 233, 33)))
        else:
            break    
        

    #pedir categoria
    category = input(colored(f"\nDe que categoria financiera es su {type_record}{categories} > ", (255, 233, 33))).capitalize
    
    
    #pedir fecha
    print(colored("\nFecha de registro con formato dd/mm/aaaa", (255, 233, 33)))
    date = input(colored("Ingrese la fecha con la que quiere registrar el registro > ", (255, 233, 33))).split("/")
        
    #Bucle por si la fecha es invalida.
    while not check_date(date):
        print("Fecha invalida, vuelve a intentarlo.")
        date = input(colored("Ingrese la fecha con la que quiere registrar el registro > ", (255, 233, 33))).split("/")
    
    
    #registrarlo en records correctamente
    if type_record == "ingreso":
        income_records[type_record + "_" + str(len(income_records) + 1)] = [value, category, date]
    if type_record == "gasto":
        expense_records[type_record + "_" + str(len(expense_records) + 1)] = [-value, category, date]
    
    
    #confirmar al usuario el exito del procedimiento
    print(colored("\nRegistro exitoso!", (255, 233, 33)))
    
     
def finance_summary():
    """Muestra un resumen mensual financiero basico.
    """
    #Se obtiene el el diccionario con los meses existentes y sus correspondientes registros
    date_records = check_months()     
           
           
    #Si no hay registros no se puede sacar resumen mensual.       
    if len(income_records) < 1 and len(expense_records) < 1:
        print(colored("No hay registros guardados.", (255, 233, 33)))
        return None
        
               
    #Mostrar todas las fechas existentes, luego pedir un mes.
    print(colored("Elige el mes del que quieres ver el resumen mensual: \n", (255, 233, 33)))
    for i in date_records:
        print(colored(i, (255, 233, 33)), "\n")
        
    opc_date = input(colored("Mes_Años > ", (255, 233, 33)))
    
    #Bucle por si elige una opcion invalida.
    while opc_date not in date_records:
        print(colored("\nOpcion no existente, intentalo de nuevo.", (255, 233, 33)))
        opc_date = input(colored("Opcion número > ", (255, 233, 33)))


    #obtener los ingresos y gastos brutos, declarar funcion para calcular las ganancias netas.
    ingresos_brutos = funcion_ingresos_brutos(date_records, opc_date)
    gastos_brutos = funcion_gastos_brutos(date_records, opc_date) 
    ganancias_netas = ingresos_brutos + gastos_brutos
    

    #Mostrar el resumen mensual
    print(colored("\n>> INGRESOS <<\n", (255, 233, 33)))        
    if len(income_records) == 0:
        print(colored("Sin ingresos", (255, 233, 33)))
    if len(income_records) > 0:    
        for i in date_records[opc_date]:
            try:
                print(colored(f"{i}: {income_records[i][0]}$", (255, 233, 33)))
            except KeyError:
                continue
        print(colored("-"*31, "black"))
        print(colored(f"Ingresos Brutos: {ingresos_brutos}", (255, 233, 33)))           
 
    
    print(colored("\n>> GASTOS <<", (255, 233, 33)), "\n")
    if len(expense_records) == 0:
        print(colored("Sin gastos", (255, 233, 33)))
    if len(expense_records) > 0:    
        for i in date_records[opc_date]:
            try:
                print(colored(f"{i}: {expense_records[i][0]}$", (255, 233, 33)))
            except KeyError:
                continue
        print(colored("-"*31), "black")
        print(colored(f"Gastos Brutos: {gastos_brutos}", (255, 233, 33)))
    
    print(colored(">> GANANCIAS NETAS <<", (255, 233, 33)))
    print(colored(f"\nGanancias Netas: {ganancias_netas}", (255, 233, 33)))
    
      
def finance_edit():
    """Permite editar registros financieros.
    """
    #Sacar el tipo de registro que el usuario editara.
    type_record = record_type()
    
    #Sacar el registro preciso a editar
    record = edit_record(type_record)
    
    
    #Mostrar las subopciones disponibles
    print(colored(f"\n1 > Editar valor de {type_record}.", (255, 233, 33)))
    print(colored("2 > Editar categoria.", (255, 233, 33)))
    print(colored("3 > Editar Fecha.", (255, 233, 33)))
    print(colored("4 > Eliminar.", (255, 233, 33)))
    
    opc_edit = input(colored("Opción número > ", (255, 233, 33)))
    
    while opc_edit not in ["1","2","3","4"]:
        print(colored("\nEleccion inexistente, intentalo de nuevo.", (255, 233, 33)))
        opc_edit = input(colored("Opción número > ", (255, 233, 33)))
        
    
    #Elecciones de el submenu con condiciona match
    match opc_edit:
        
        case "1":
            print("\n")
            
            if type_record == "ingreso":
                income_records[record][0] = float(input(colored(f"Cual sera el valor nuevo de {record}, el actual es {income_records[record][0]} > ", (255, 233, 33))))     
            
            else:
                expense_records[record][0] = -float(input(colored(f"Cual sera el valor nuevo de {record}, el actual es {expense_records[record][0]} > ", (255, 233, 33))))
            
            print("\n")
            
            
        case "2":
            print("\n")
            
            if type_record == "ingreso":
                income_records[record][1] = input(colored(f"Cual sera la nueva categoia de {record}, la actual es {income_records[record][1]} > ", (255, 233, 33)))     
            
            else:
                expense_records[record][0] = input(colored(f"Cual sera la nueva categoria de {record}, la actual es {expense_records[record][1]} > ", (255, 233, 33)))
            
            print("\n")
            
        case "3":
            print("\n")
            print(colored("Nueva fecha, formato: dd/mm/aaaa", (255, 233, 33)))
            
            if type_record == "ingreso":
                new_date = input(colored(f"Cual sera el valor nuevo de {record}, el actual es {income_records[record][0]} > ", (255, 233, 33))).split("/")     
                
                while not check_date(new_date):
                    print(colored("Fecha invalida, intentalo de nuevo.", (255, 233, 33)))
                    new_date = input(colored(f"Cual sera el valor nuevo de {record}, el actual es {income_records[record][0]} > ", (255, 233, 33))).split("/")
                
                income_records[record][2] = new_date    
            
            else:
                new_date = input(colored(f"Cual sera el valor nuevo de {record}, el actual es {expense_records[record][0]} > ", (255, 233, 33))).split("/")     
                
                while not check_date(new_date):
                    print(colored("Fecha invalida, intentalo de nuevo.", (255, 233, 33)))
                    new_date = input(colored(f"Cual sera el valor nuevo de {record}, el actual es {expense_records[record][0]} > ", (255, 233, 33))).split("/")
                
                expense_records[record][2] = new_date
            
            print("\n")
            
        
        case _:
            print("Si llegaste aqui debes ser hacker =)")
                
    
    print(colored("Registro editado con exito!", (255, 233, 33)))




