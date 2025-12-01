/* Esercize ventisei

    Mostrar los meses del año, pidiendole al usuario un numero entre (1-12)
    y mostrar el mes al que corresponde

*/

#include<stdio.h>

int main(void)
{
    int num_mes;

    printf("\nDigita un numero del 1 al 12: "); scanf("%i", &num_mes);

    switch (num_mes)
    {
        case 1: printf("\nEl mes 1 del año es enero\n"); break;
        case 2: printf("\nEl mes 2 del año es febrero\n\n"); break;
        case 3: printf("\nEl mes 3 del año es marzo\n\n"); break;
        case 4: printf("\nEl mes 4 del año es abril\n\n"); break;
        case 5: printf("\nEl mes 5 del año es mayo\n\n"); break;
        case 6: printf("\nEl mes 6 del año es junio\n\n"); break;
        case 7: printf("\nEl mes 7 del año es julio\n\n"); break;
        case 8: printf("\nEl mes 8 del año es agosto\n\n"); break;
        case 9: printf("\nEl mes 9 del año es septiembre\n\n"); break;
        case 10: printf("\nEl mes 10 del año es octubre\n\n"); break;
        case 11: printf("\nEl mes 11 del año es noviembre\n\n"); break;
        case 12: printf("\nEl mes 12 del año es diciembre\n\n"); break;
        default: printf("\nNumero de mes invalidos\n"); break;
    }

    return 0;
}