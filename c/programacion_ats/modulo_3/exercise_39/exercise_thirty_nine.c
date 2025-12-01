/* Esercizio trentanove

    Hacer un programa que sue la suma de factoriales hasta n
    
*/

#include <stdio.h>

int main(void)
{
    int n = 0, factorial = 1, suma = 0;
    printf("Digita un numero: ");
    scanf("%i", &n);

    for (int i = 1; i <= n; i++)
    {
        factorial *= i;
        suma += factorial;
    }

    printf("La suma de factoriales es %i\n", suma);

    return 0;
}