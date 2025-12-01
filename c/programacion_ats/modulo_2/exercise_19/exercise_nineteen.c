/* Esercize diecinove

    Ingresar por teclado el nombre y el signo de cualquier persona e imprima,
    el nombre solo si la persona es signo Aries, caso contrario imprima no es signo Aries

*/

#include<stdio.h>
#include<string.h>

int main(void)
{
    char name[60], signo[10];

    printf("\nDigita tu nombre: "); 
    if (fgets(name, sizeof(name), stdin) != NULL)
    {
        name[strcspn(name, "\n")] = 0;
    }

    printf("\nDigita tu signo: ");
    if (fgets(signo, sizeof(signo), stdin) != NULL)
    {
        signo[strcspn(signo, "\n")] = 0;
    }


    if (strcmp(signo, "Aries") == 0 || strcmp(signo, "aries") == 0)
    {
        printf("\nTu signo es aries\n");
    }
    else
    {
        printf("\nTu signo no es aries\n");
    }

    return 0;
}