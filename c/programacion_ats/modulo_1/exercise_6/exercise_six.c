/* Esercize sei

    <calcula la media aritmetica de 3 numeros cualesquiera
*/

#include<stdio.h>

int main(void)
{
    int number_1, number_2, number_3, media;

    printf("\nDigita un numero: "); scanf("%i", &number_1);
    printf("\nDigita otro numero: "); scanf("%i", &number_2);
    printf("\nDigita un ultimo numero: "); scanf("%i", &number_3);
    
    media = (number_1 + number_2 + number_3) / 3;

    printf("\nLa media de esos tres numeros es: %i\n", media);
    
    return 0;
}