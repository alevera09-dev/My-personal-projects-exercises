/* Esercizio quarantta

    Hacer un programa que haga la serie fibonacci hasta n
    
*/

#include <stdio.h>

int main(void)
{
    int n = 0, fibonacci = 0;
    printf("Digita el valor de n: ");
    scanf("%i", &n);

    for (int i = 1; i <= n; i++)
    {
        if (i <= 2)
        {
            fibonacci += 1;
        }
        else
        {
            fibonacci += i-1;
        }
        
    }

    printf("La suma total es %i\n", fibonacci);

    return 0;
}