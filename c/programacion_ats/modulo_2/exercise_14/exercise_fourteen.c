/* Esercize quattordici

    Comprobar si un numero digitado por el usuario es positivo o negativo

*/

#include<stdio.h>

int main(void)
{
    int number;

    printf("\nDigita un numero: "); scanf("%i", &number);

    if (number < 0)
    {
        printf("\n El numero es negativo\n");
    }
    else if (number > 0)
    {
        printf("\nEl numero es positivo\n");
    }
    else
    {
        printf("\nEl numero es cero\n");
    }

    return 0;
}