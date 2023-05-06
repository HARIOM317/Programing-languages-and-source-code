#include<iostream>

using namespace std;

int main()
{
    int n;
    cout<<"Enter a number"<<endl;
    cin>>n;

    cout<<"\n\n";

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n+1-i; j++){
            cout<<j<<" ";
        }cout<<endl;
    }
    cout<<"\n\n";
    return 0;
}