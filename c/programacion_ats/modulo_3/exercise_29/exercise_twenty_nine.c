/* Esercizio ventinove

    Suma los numrros hasta n

*/

#include <stdio.h>

int main(void)
{
    int n = 0, suma = 0;

    printf("Digita el valor de n: ");
    scanf("%i", &n);

    int i = 0;

    while (i <= n)
    {
        suma += i;
        i++;
    }

    printf("\nLa suma de todos los numeros es: %i\n", suma);

    return 0;
}