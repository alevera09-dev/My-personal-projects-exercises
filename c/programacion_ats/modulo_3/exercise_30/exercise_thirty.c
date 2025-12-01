/* Esercizio trenta

    Digite un numero, si el numero supera a 10, multiplique los 10 primeros numeros sino sumelos

*/

#include <stdio.h>

int main(void)
{
    int number = 0, sum = 0, mult = 1;

    printf("Digite un numero: ");
    scanf("%i", &number);

    if (number > 10)
    {
        int i = 1;

        while (i < 11)
        {
            mult *= i;
            i++; 
        }
        printf("La multiplicacion es: %i\n", mult);
        
    }
    else
    {
        int i = 0;

        while (i <= number)
        {
            sum += i;
            i++;
        }
        
        printf("La suma es: %i\n", sum);
    }

    return 0;
}