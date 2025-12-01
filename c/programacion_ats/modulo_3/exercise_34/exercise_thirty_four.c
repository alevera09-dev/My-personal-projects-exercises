/* Esercizio trentaquattro

    Suma pares de n hasta m

*/

#include <stdio.h>

int main(void)
{
    int n = 0, m = 0, suma = 0;
    printf("Digita el valor de n: ");
    scanf("%i", &n);
    printf("\nDigita el valor de m: ");
    scanf("%i", &m);

    while (n <= m)
    {
        suma += n;
        n++;
    }
    printf("La suma total es %i\n", suma);

    return 0;
}