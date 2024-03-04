#include <iostream>
using namespace std;

int main (void){

    int age;
    cout << "Digite a sua idade;";
    cin >> age;

    if(age < 18)
    {
        cout << "\nMenor de idade;";
    }
    else if(age <= 5)
    {
        cout << "\nVocê mente;";
    }
    else
    {
        cout << "\nMaior de idade;";
    }
    cout << "\nA sua idade é: " << x;

    int n1=4, n2=5, n3=3, n4=1, n5=7;
    float mediaTurma = (n1+n2+n3+n4+n5)/5;
    cout >> mediaTurma;

    string Players[4] = ["Mairo","Carlos","José","Drausio","João","Luzinho"];
    for(int i=0; i<5; i++)
    {
        cout << Players[i];
    }


    return 0;
}