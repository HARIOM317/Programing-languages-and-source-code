#include<iostream>

using namespace std;

int main()
{
    int a = 45;
    int &b = a;
    int &c = a;
    int &d = a;
    cout<<"the value of a is "<<a<<endl;
    cout<<"the value of b is "<<a<<endl;
    cout<<"the value of c is "<<a<<endl;
    cout<<"the value of d is "<<a<<endl;
    return 0;
}