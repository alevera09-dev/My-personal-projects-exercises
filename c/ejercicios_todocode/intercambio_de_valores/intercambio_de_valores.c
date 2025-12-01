#include <stdio.h>

int main(void)
{
    int n1 = 35, n2 = 20, aux = 0;

    printf("\nn1 vale %i y n2 vale %i", n1, n2);

    aux = n1;
    n1 = n2;
    n2 = aux;

    printf("\nn1 vale %i y n2 vale %i\n", n1, n2);

    return 0;
}