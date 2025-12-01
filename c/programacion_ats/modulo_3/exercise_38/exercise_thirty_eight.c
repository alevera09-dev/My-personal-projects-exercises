/* Esercizio trentotto

    Hallar el factoria de n
    
*/

#include <stdio.h>

int main(void)
{
    int n = 0, factorial = 1;
    printf("Digita un numero: ");
    scanf("%i", &n);

    for (int i = 1; i <= n; i++)
    {
        factorial *= i;
    }

    printf("El numero factorial de %i es %i\n", n, factorial);

    return 0;
}