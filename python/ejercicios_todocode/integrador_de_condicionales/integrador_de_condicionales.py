"""
Una pequeña despensa desea calcular los sueldos de sus empleados. Los puestos de los mismos pueden teer 3 categrias:

    1. Repositor
    2. Cajero
    3. Supervisor

* Los repositores cobran $15_890 + bono del 10%
* Los cajeros cobran $25_630.89 fijos
* Los supervisores cobran $35_560.20 en bruto al cual se les descuenta un 11% de jubilacion

Se necesita un programa que, dependiendo del tipo de empleado del que se trate,
calcule y muestre en pantalla el correspondiente sueldo
"""

while True:
    print("---SUELDOS---")
    print("\n1. Repositor.")
    print("2. Cajero.")
    print("3. Supervisor.")
    opc = int(input("\n\Elige un tipo de empleado para ver su sueldo: "))
    
    sueldo = 0.0
    if opc == 1:
        sueldo = 15890.0 * 1.10
        print(f"\nEl sueldo que cobran los repositores es: {sueldo:.2f}\n")
    elif opc == 2:
        sueldo = 25630.89
        print(f"\nEl sueldo que cobran los repositores es: {sueldo:.2f}\n")
    elif opc == 3:
        sueldo = 35560.20 - (35560.20 * 0.11)
        print(f"\nEl sueldo que cobran los repositores es: {sueldo:.2f}\n")
    elif opc == 4:
        print("\nAdios, vuelve pronto!!!\n")
        break
    else:
        print("\nERROR: esperaba un numero de 1 a 3, amigo las opciones estan claras!!!, vuelve a intentarlo\n")