/* Esercizio trentasei

    Hacer un arbol con '*' del tipo: ejemplo:
        
        Digite el numero de filas: 5
                    *
                   * *
                  * * *
                 * * * *
                * * * * * 
*/

#include <stdio.h>

int main(void)
{
    int height = 0;
    printf("Digite la altura del arbol: ");
    scanf("%i", &height);

    for (int fila = height; fila > 0; fila--)
    {
        for (int space = 1; space < fila; space++)
        {
            printf(" ");
        }
        for (int star = height; star > fila; star--)
        {
            printf("* ");
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}