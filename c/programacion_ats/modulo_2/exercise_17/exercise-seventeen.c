/* Esercize diecisette

    Comprobar el amyor de dos numeros

*/

#include<stdio.h>

int main(void)
{
    int n1, n2;

    printf("\nDigita un numero: "); scanf("%i", &n1);
    printf("\nDigita otro numero: "); scanf("%i", &n2);

    if (n1 > n2)
    {
        printf("\n%i es mayor a %i\n", n1, n2);
    }
    else
    {
        printf("\n%i es mayor a %i\n", n2, n1);
    }

    return 0;
}