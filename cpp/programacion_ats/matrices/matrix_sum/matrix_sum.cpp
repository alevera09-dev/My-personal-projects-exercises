/*6. Realice un programa que calcule la suma de dos matrices cuadradas de 3x3.*/

#include <iostream>

int main(void)
{
    using std::cout, std::endl;
    
    int matrix_1[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrix_2[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int matrix_sum[3][3];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j];
        }
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << matrix_sum[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}