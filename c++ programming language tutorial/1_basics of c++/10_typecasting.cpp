#include<iostream>

using namespace std;

int main()
{
    int a = 10;
    char b = 'h';
    float c = 20.45;
    a = a+b;
    cout<<"Implicit conversion from character to integer: "<<a<<endl;
    c = c+a;
    cout<<"Implicit conversion from integer to float: "<<c<<endl;
    return 0;
}