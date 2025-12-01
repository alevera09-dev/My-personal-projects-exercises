/* Esercize uno

    Pedir due numeri al usuario y sumarlos. restarlos, multiplicarlos y dividirlos.
*/

#include <stdio.h>

int main(void)
{
    int n1;
    int n2;

    printf("Digita un número: ");
    scanf("%i", &n1);

    printf("Digita otro número: ");
    scanf("%i", &n2);

    int suma = n1 + n2;
    int resta = n1 - n2;
    int multiplicacion = n1 * n2;
    int division = n1 / n2;

    printf("\nSuma: %i", suma);
    printf("\nResta: %i", resta);
    printf("\nMultiplicacion: %i", multiplicacion);
    printf("\nDivision: %i\n", division);

    return 0;
}