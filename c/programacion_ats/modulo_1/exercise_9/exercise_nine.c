/* Esercize nove

    Calcular el nuevo salario de un obrero si obtuvo un incremento del 25%
    sobre su salario anterior.

*/

#include<stdio.h>

int main(void)
{
    float salario, incremento = 0.25;

    printf("\nDigita tu salario actual: "); scanf("%f", &salario);

    salario = salario * (incremento + 1);

    printf("\nEl salario aumentado es: %.2f\n", salario);

    return 0;
}