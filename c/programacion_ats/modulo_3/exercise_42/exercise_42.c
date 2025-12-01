/* Esercizio quaranttadue

    Hacer un bucle do while para imprimir las letras minusculas del alfabeto

*/

#include <stdio.h>

int main(void)
{
    char letra = 'a';
    
    do
    {
        if (letra == 'a')
        {
            printf("%c\n", letra);
        }
        else
        {
            printf("%c\n", letra);
        }
        letra ++;
    } while (letra <= 'z');
    

    return 0;
}