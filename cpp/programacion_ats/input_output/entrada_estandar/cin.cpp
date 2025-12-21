/*3. Realice un programa que lea de la entrada estandar los siguientes datos de una persona

    Edad: dato de tipo entero
    Sexo: dato de tipo caracter
    Altura en metros: dato de tipo real

Tras leer los datos, el programa debe mostrarlos en la salida estandar
*/

#include <iostream>

using namespace std;

int main(void)
{
    //inputs
    int age;
    cout << "Digite su edad: ";
    cin >> age;

    char gender;
    cout << "Digite su genero(M/F): ";
    cin >> gender;

    float height;
    cout << "Digite su altura: ";
    cin >> height;

    //outputs
    cout << "\nEDAD: " << age << endl;
    cout << "GENERO: " << gender << endl;
    cout << "ESTATURA: " << height << endl;

    return 0;
}