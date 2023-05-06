#include<iostream>

int isPowerOf2(int n){
    return (n && !(n & n-1));
}

using namespace std;

int main()
{
    cout<<isPowerOf2(32)<<endl;
    return 0;
}