/*2. Realiza un programa que defina una matriz de 3x3 y escriba un ciclo para que muestre
la diagonal principl de la matriz*/

#include <iostream>

int main(void)
{
    using std::cout, std::endl;
    int arr_3d[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (i == j)
            {
                cout << '[' << i << ']' << '[' << j << ']'<< '(' << arr_3d[i][j] << ')' << endl;
            }
        }
    }
    return 0;
}