/*

Una pequeña despensa desea calcular los sueldos de sus empleados. Los puestos de los mismos pueden teer 3 categrias:

    1. Repositor
    2. Cajero
    3. Supervisor

* Los repositores cobran $15_890 + bono del 10%
* Los cajeros cobran $25_630.89 fijos
* Los supervisores cobran $35_560.20 en bruto al cual se les descuenta un 11% de jubilacion

Se necesita un programa que, dependiendo del tipo de empleado del que se trate,
calcule y muestre en pantalla el correspondiente sueldo

*/

#include <stdio.h>

int main(void)
{
    while (1)
    {
        printf("\n---SUELDOS---");
        printf("\n\n1. Repositor.");
        printf("\n2. Cajero.");
        printf("\n3. Supervisor.");
        printf("\n4. Salir.");
        printf("\n\nElige un tipo de empleado para ver su sueldo: ");
        int opc = 0;
        scanf("%i", &opc);

        float sueldo = 0.0;
        if (opc == 1)
        {
            sueldo = 15890.0 * 1.10;
            printf("\nEl sueldo que cobran los repositores es: %.2f\n", sueldo);
        }
        else if (opc == 2)
        {
            sueldo = 25630.89;
            printf("\nEl sueldo que cobran los cajeros es: %.2f\n", sueldo);
        }
        else if (opc == 3)
        {
            sueldo = 35560.20 - (35560.20 * 0.11);
            printf("\nEl sueldo que cobran los repo es: %.2f\n", sueldo);
        }
        else if (opc == 4)
        {
            printf("\nAdios, vuelve pronto!!!\n");
            break;
        }
        else
        {
            printf("\nERROR: esperaba un numero de 1 a 3, amigo las opciones estan claras!!!, vuelve a intentarlo\n");
        }
    }

    return 0;
}