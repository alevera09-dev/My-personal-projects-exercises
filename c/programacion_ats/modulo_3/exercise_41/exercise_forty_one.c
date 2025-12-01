/* Esercizio quaranttuno

    hacer un programa que muestre todos los numeros pares de 1 hasta n y la suma de esos numeros
    
*/

#include <stdio.h>

int main(void)
{
    int n = 0, pares = 0, suma_pares = 0;
    printf("Digita el valor de n: ");
    scanf("%i", &n);

    for (int i = 2; i <= n; i += 2)
    {
        pares++;
        suma_pares += i;
    }

    printf("Se encontraron %i numeros pares y la suma de esos numeros es: %i\n", pares, suma_pares);

    return 0;
}