#include<iostream>

using namespace std;

int main()
{
    int * ptr = NULL;
    cout<<"The value of null pointer is: "<<ptr<<endl;
    int a = 12;
    ptr = &a;
    cout<<"The value of pointer is: "<<*ptr<<endl;
    return 0;
}