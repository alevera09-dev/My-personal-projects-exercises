/* Esercize ventiquattro

    Seleccionar un tipo de vehiculo e indicar el peaje a pagar
    segun un valor numerico

    1 - turismo, peaje = $500
    2 - autobus, peaje = $3000
    3 - motocicleta, peaje = $300
    caso contrario = Vehiculo no autorizado

*/

#include<stdio.h>

int main(void)
{
    char opc;

    printf("\n\tPEAJE\n");
    printf("\nElige una de estas opciones dependiento del tipo de vehiculo\n");
    printf("\n1.Turismo");
    printf("\n2.Autobus");
    printf("\n3.Motocicleta");
    printf("\n\nOpcion numero > "); scanf("%c", &opc);

    switch (opc)
    {
        case '1': printf("\nEl peaje es de $500\n"); break;
        case '2': printf("\nEl peaje es de $3000\n"); break;
        case '3': printf("\nEl peaje es de $300\n"); break;
        default: printf("\nVehiculo no autorizado\n"); break;
    }
    return 0;
}