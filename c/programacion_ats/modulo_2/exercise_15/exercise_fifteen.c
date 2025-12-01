/* Esercize quindici

    Visualizar la tarifa de la luz segun el gasto de corriente electrica
    Para un gasto menor de 1.000Kwxh la tarifa es 1.2, entre 1.000 y 1.850Kwxh es 1.0 y mayor de 1.850Kwxh 0.9.

*/

#include<stdio.h>

int main(void)
{
    float gasto, tarifa;

    printf("\nDigita el gasto de corriente electrica: "); scanf("%f", &gasto);

    if (gasto < 1000)
    {
        tarifa = 1.2;
    }
    else if (gasto > 1850)
    {
        tarifa = 0.9;
    }
    else 
    {
        tarifa = 1.0;
    }

    printf("\nLa tarifa a pagar es: %.2f\n", tarifa);

    return 0;
}