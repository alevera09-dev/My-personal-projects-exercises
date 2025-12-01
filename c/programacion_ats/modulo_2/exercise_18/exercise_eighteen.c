/*

    Ingrese un numero y calcule e imprima su raiz cuadrada.
    Si el numero es negativo imprima el numero y un mensaje
    que diga "tiene raiz imaginaria"

*/

#include<math.h>
#include<stdio.h>

int main(void)
{
    double number, raiz_cuadrada;

    printf("\nDigite un numero: "); scanf("%lf", &number);

    if (number > 0)
    {
        raiz_cuadrada = sqrt(number);
        printf("\n%.2lf\n", raiz_cuadrada);
    }
    else if (number < 0)
    {
        printf("\n%.2lf tiene raiz imaginaria\n", number);
    }
    else
    {
        printf("\nEs cero\n");
    }

    return 0;
}