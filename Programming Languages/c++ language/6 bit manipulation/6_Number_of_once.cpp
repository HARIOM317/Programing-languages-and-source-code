#include<iostream>

int numberOfOnes(int n){
    int count = 0;
    while(n){
        n = n & (n-1);
        count++;
    }
    return count;
}

using namespace std;

int main()
{
    cout<<numberOfOnes(119)<<endl;
    return 0;
}