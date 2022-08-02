#include<iostream>

using namespace std;

int factorial(int value){
    int fact = 1;
    for (int i = 2; i <= value; i++)
    {
        fact*=i;
    }
    return fact;   
}

int main()
{
    int n, r;
    cout<<"Enter value of n and r to calculate nCr :  ";
    cin>>n>>r;

    int ans = factorial(n)/(factorial(r)*factorial(n-r));
    cout<<"nCr = "<<ans;

    return 0;
}