/* Esercizio trentatre

    Hacer la serie: 1-2+3-4... n

*/

#include <stdio.h>

int main(void)
{
    int n = 0;
    printf("Digita el valor de n: ");
    scanf("%i", &n);

    int i = 1, suma_impares = 0, suma_pares = 0;
    while (i <= n)
    {
        if (n % 2 == 0)
        {   
            int ne = i * (-1);
            suma_pares += -i;
        }
        else
        {
            suma_impares += i;
        }

        i++;
    }

    int suma = suma_pares + suma_impares;
    printf("La suma total es: %i\n", suma);

    return 0;
}