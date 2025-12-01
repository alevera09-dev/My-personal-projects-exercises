/* Esercize dieci

    Un alumno desea saber cual sera su calificacion final en la materia de Algoritmos.
    Dicha calificacion se compone de los siguientes porcentajes:

        * 55% de promedio de sus tres calificaciones parciales.
        * 30% de la calificacion del examen final.
        * 15% de la calificacion de un trabajo final.

*/

#include<stdio.h>

int main(void)
{
    float c1, c2, c3, promedio_parciales, examen_final, trabajo_final, calificacion_final;

    printf("\nDigita la primera calificacion parcial: "); scanf("%f", &c1);
    printf("\nDigita la segunda calificacion parcial: "); scanf("%f", &c2);
    printf("\nDigita la tercera calificacion parcial: "); scanf("%f", &c3);
    printf("\nDigita la calificacion del examen final: "); scanf("%f", &examen_final);
    printf("\nDigita la calificacion del trabajo final: "); scanf("%f", &trabajo_final);

    promedio_parciales = c1 + c2 + c3 / 3;
    
    calificacion_final = (promedio_parciales * 0.55) +
                         (examen_final * 0.30) + 
                         (trabajo_final * 0.15);

    printf("\nTu calificacion final de Algoritmos es: %.1f\n", calificacion_final);

    return 0;
}