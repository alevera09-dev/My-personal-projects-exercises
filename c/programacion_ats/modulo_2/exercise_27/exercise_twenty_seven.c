/* Esercize ventisette

    Hacer un programa que simule un cajero automatico con un saldo inicial de $1000

*/

#include<stdio.h>

int main(void)
{
    int opc;
    float saldo = 1000.0, ingreso, retiro;

    printf("\n\tCAJERO AUTOMATICO EN C.\n");
    printf("\n1 >> Depositar dinero.");
    printf("\n2 >> Retirar dinero.");
    printf("\n3 >> Ver saldo.");
    printf("\n4 >> Salir.");

    printf("\n\nOpcion numero > "); 
    scanf("%i", &opc);


    switch (opc)
    {
        case 1:
            printf("\n\nCuanto ingresaras? > ");
            scanf("%f", &ingreso);
            saldo += ingreso;
            printf("\nIngreso exitoso, ahora tienes $%.2f en tu cuenta\n\n", saldo);
            break;

        case 2:
            printf("\n\nCuanto retiraras? > ")
            scanf("%f", &retiro);
            saldo -= retiro;
            printf("\nIngreso exitoso, ahora tienes $%.2f en tu cuenta\n\n", saldo);
            break;

        case 3:
            printf("\n\nTu saldo bancario actual es: $%.2f\n\n", saldo);
            break;

        case 4:
            break;

        default: 
            printf("\n\nOpcion invalida!\n");
    }


    return 0;
}