/* Esercizio trentuno

    Multiplos de 3 desde 1 hasta n

*/

#include <stdio.h>

int main(void)
{
    int n = 0;

    printf("Digita el valor de n: ");
    scanf("%i", &n);

    int i = 1;

    while (i < n)
    {
        if (i % 3 == 0)
        {
            printf("\n%i\n", i);
        }
        i++;
    }

    return 0;
}