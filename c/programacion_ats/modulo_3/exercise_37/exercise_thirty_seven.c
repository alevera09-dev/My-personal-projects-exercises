/* Esercizio trentasette

    Haz un programa que determine si un numero es primo o no
    
*/

#include <stdio.h>

int main(void)
{
    int n = 0, divisibles = 0;
    printf("Digita un numero: ");
    scanf("%i", &n);

    for (int i = 2; i <= n; i++)
    {
        if (n % i == 0)
        {
            divisibles++;
        }
    }

    printf("\nEl numero es ");
    (n == 1) ? printf("1\n") : (divisibles > 1) ? printf("no primo\n") : printf("primo\n");

    return 0;
}