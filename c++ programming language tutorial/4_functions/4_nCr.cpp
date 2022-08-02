#include<iostream>

using namespace std;

int fact(int n){
    int factorial = 1;
    for(int i=2; i<=n; i++){
        factorial = factorial*i;
    }
    return factorial;
}

int main()
{
    int n, r;
    cout<<"Enter values of n and r "<<endl;
    cin>>n>>r;
    int ans = fact(n)/(fact(n-r)*fact(r));
    cout<<"nCr = "<<ans<<endl;
    return 0;
}