/* Esercize sedici

    Determina si un numero es par o impar

*/

#include<stdio.h>

int main(void)
{
    int number;

    printf("\nDigita un numero: "); scanf("%i", &number);

    if (number % 2 == 0)
    {
        printf("\nElnumero es par\n");
    }
    else
    {
        printf("\nElnumero es impar\n");
    }

    return 0;
}