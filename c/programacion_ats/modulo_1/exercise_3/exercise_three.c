/* Esercize tre

    Sacar la hipotenusa de un triangulo rectangulo,
    pidiendo al usuario el valor de los due catetos

*/

#include<math.h>
#include<stdio.h>

int main(void)
{
    double cateto_1, cateto_2, hipotenusa;

    printf("\nDigita dos catetos de un triangulo rectangulo: \n");
    scanf("%lf %lf", &cateto_1, &cateto_2);

    hipotenusa = sqrt(pow(cateto_1, 2) + pow(cateto_2, 2));

    printf("La hipotenusa de el trianulo rectangulo es: %.lf\n", hipotenusa);

    return 0;
}