/* Esercize undeci

    Calcular la cantidad de segundos que estan incluidos en el numero de horas,
    minutos y segundos ingresados por el usuario.

*/

#include<stdio.h>

int main(void)
{
    int horas, minutos, segundos, total_segundos;

    printf("\nDigita un valor de hora/s: "); scanf("%i", &horas);
    printf("\nDigita un valor de minuto/s: "); scanf("%i", &minutos);
    printf("\nDigita un valor de segundo/s: "); scanf("%i", &segundos);

    total_segundos = (horas * 3600) + (minutos * 60) + segundos;
              
    printf("\nLos segundos totales son: %i\n", total_segundos);

    return 0;
}