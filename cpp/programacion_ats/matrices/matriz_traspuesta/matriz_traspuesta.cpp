/*5. Realice un programa que lea una matriz de 3x3 y cree su matriz transpuesta.
La matriz traspuesta es aquella en la que la columna i era la fila i de la matriz original. */

#include <iostream>

int main(void)
{
    using std::cout, std::endl;

    int matriz[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int transpuesta[3][3];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            transpuesta[i][j] = matriz[j][i];
        }
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << transpuesta[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}