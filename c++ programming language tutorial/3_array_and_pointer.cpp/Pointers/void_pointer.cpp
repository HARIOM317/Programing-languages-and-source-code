#include<iostream>

using namespace std;

int main()
{
    int n = 45;
    float f = 12.2145;
    char c = 'H';
    void *ptr;
    ptr = &n;
    cout<<"The value of n is: "<<*((int*)ptr)<<endl;
    ptr = &f;
    cout<<"The value of f is: "<<*((float*)ptr)<<endl;
    ptr = & c;
    cout<<"The value of c is: "<<*((char*)ptr)<<endl;
    return 0;
}