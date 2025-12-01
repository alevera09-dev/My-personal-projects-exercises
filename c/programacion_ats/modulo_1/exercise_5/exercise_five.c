/* Esercize cinque

    Hacer un programa que calcule areas de trapecios 

    Formula de area de trapecios: area = ((base mayor + base menor) * altura) / 2
*/

#include<stdio.h>

int main(void)
{
    float base_mayor, base_menor, altura, area;

    printf("\nDigita la base mayor del trapecio: "); scanf("%f", &base_mayor);
    printf("\nDigita la base menor del trapecio: "); scanf("%f", &base_menor);
    printf("\nAhora digita la altura del trapecio: "); scanf("%f", &altura);

    area = ((base_mayor + base_menor) * altura) / 2;

    printf("\nEl area del trapecio es: %.2f\n", area);
    
    return 0;
}