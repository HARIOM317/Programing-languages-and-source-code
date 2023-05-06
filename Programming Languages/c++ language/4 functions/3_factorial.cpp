#include<iostream>

using namespace std;

int fact(int n){
    int factorial = 1;
    for(int i = 2; i <= n; i++){
        factorial = factorial*i;
    }
    return factorial;
}

int main()
{
    int n;
    cout<<"Enter a number for factorial"<<endl;
    cin>>n;
    int ans = fact(n);
    cout<<"Factorial is = "<< ans<<endl;
    return 0;
}