/* Esercizi due

    Convertir grados celsius a farenheit

*/

#include<stdio.h>

int main(void)
{
    int celcius;

    printf("Digita los grados celcius que quieres convertir a farenheit: ");
    scanf("%i", &celcius);

    int farenheit = ((celcius * 9) / 5) + 32;

    printf("\n%i grados celcius son %i grados farenheit\n\n", celcius, farenheit);

    return 0;
}