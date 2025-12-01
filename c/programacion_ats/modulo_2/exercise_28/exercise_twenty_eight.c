/* Esercize ventotto

    Hacer un menu que considere las siguientes opciones
    caso 1: Cubo de un numero
    caso 2: Numero par o impar
    caso 3: salir

*/

#include<math.h>
#include <stdio.h>

int main(void)
{
    int opc;
    double num;

    printf("\n\tMENU\n");
    printf("\n1. Cubo de un numero");
    printf("\n2. Numero par o impar");
    printf("\n3. Salir");
    printf("\n\nOpcion numero > ");
    scanf("%i", &opc);

    switch(opc)
    {
        case 1:
            printf("\n\nDigita un numero que quieras saber su cubo: ");
            scanf("%lf", &num);
            printf("\nEl cubo es %.2lf\n\n", pow(num, 3));
            break;    

        case 2:
            int num_int = (int) num; 

            printf("\n\nDigita un numero para saber si es par o impar: ");
            scanf("%i", &num_int);
            
            if (num_int % 2 == 0)
            {
                printf("\n%i es par\n\n", num_int);
            }
            else
            {
                printf("\n%i es impar\n\n", num_int);
            }
        
        case 3:
            break;
         
        default:
            printf("Opcion invalida");    
    } 

    return 0;
}