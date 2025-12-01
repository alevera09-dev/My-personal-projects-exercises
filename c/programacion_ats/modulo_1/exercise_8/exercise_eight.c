/* Esercize otto

    Dadas las horas trabajadas de una persona y el valor por hora.
    Calcular su salario e imprimirlo.

*/

#include<stdio.h>

int main(void)
{
    int horas_trabajo;
    float valor_hora, salario;

    printf("\n Digita las horas trabajadas: "); scanf("%i", &horas_trabajo);
    printf("\n Digita el valor de la hora: "); scanf("%f", &valor_hora);

    salario = valor_hora * horas_trabajo;

    printf("\nTu salario es: %.2f\n", salario);

    return 0;
}