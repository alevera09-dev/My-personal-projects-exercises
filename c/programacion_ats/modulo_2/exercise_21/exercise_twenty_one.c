/* Esercize ventuno

Hacer un programa que cierre la pantalla al oprimir 1(cerrar el programa)

*/

#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    char boton;

    printf("\nOprime 1: "); scanf("%c", &boton);

    if (boton == '1')
    {
        system("clear");
        printf("\nHa funcionado\n");
    }

    return 0;
}