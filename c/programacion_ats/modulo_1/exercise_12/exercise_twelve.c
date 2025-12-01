/* Esercize tredici

    Hacer un programa que obtenga la media geometrica de tres numeros.

    Media geometrica = sqrt(x1 * x2 * x3, ...n)

*/

#include<math.h>
#include<stdio.h>

int main(void)
{
    double n1, n2, n3, mg;

    printf("\nDigita el numero: "); scanf("%lf", &n1);
    printf("\nDigita otro numero: "); scanf("%lf", &n2);
    printf("\nDigita el ultimo numero: "); scanf("%lf", &n3);

    mg = pow(n1 * n2 * n3, 1.0/3);
    
    printf("\nLa media geometrica de los tres numeros es: %.2lf\n", mg);

    return 0;
}