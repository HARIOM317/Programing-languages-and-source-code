#include<iostream>

using namespace std;

int main()
{
    int arr[5] = {35,55,53,86,98};
    int *p = arr;
    cout<<"The value of arr[0] is "<<*p<<endl;
    cout<<"The value of arr[1] is "<<*(p+1)<<endl;
    cout<<"The value of arr[2] is "<<*(p+2)<<endl;
    cout<<"The value of arr[3] is "<<*(p+3)<<endl;
    cout<<"The value of arr[4] is "<<*(p+4)<<endl;

    return 0;
}