/* Esercize ventitre

    Dada una nota de un examen mediante un codigo escribir el literal que le
    corresponde a la nota
    
    A - Excelente
    B - Notable
    C- Aprobado
    D y F - Reprobado

*/

#include<stdio.h>

int main(void)
{
    char nota;

    printf("\nCual es tu nota?: "); scanf("%c", &nota);

    switch (nota)
    {
        case 'A': printf("\nHas aprobado de forma excelente\n"); break;

        case 'B': printf("\nHas aprobad de forma notable\n"); break;

        case 'C': printf("\nHas aprobado de forma decente\n"); break;

        case 'D':
        
        case 'F': printf("\nHas reprobado\n"); break;

        default: printf("\nEntrada incorrecta\n"); break;
    }

    return 0;
}