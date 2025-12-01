/* Esercize tredici

    Comprobar a traves de un programa si un alumno aprobo o no un
    examen (Aprueba si su nota es mayor a 10.5)

*/


#include<stdio.h>

int main(void)
{
    float grade;

    printf("\nDigita su nota: "); scanf("%f", &grade);

    if (grade >= 10.5)
    {
        printf("\nAprobado =)\n");
    }
    else
    {
        printf("\nNo aprobado =(\n");
    }

    return 0;
}