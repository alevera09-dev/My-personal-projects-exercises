/* Esercize quattro
    Hacer un programa que calcule longitudes de cicunferencia
*/

#include<stdio.h>

int main(void)
{
    const double PI = 3.1416;
    float radio, circunferencia;

    printf("Digita el radio del circulo: ");
    scanf("%f", &radio);

    circunferencia = 2 * PI * radio;

    printf("La circunferencia es: %.2f\n", circunferencia);

    return 0;
}