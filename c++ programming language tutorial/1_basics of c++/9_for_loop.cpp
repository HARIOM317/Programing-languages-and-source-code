#include<iostream>

using namespace std;

int main()
{
    int num;
    cout<<"Entre a number till you want to print even numbers"<<endl;
    cin>>num;
    for (int i = 2; i <= num; i++)
    {
        if(i%2==0){
            cout<<i;
            cout<<"\t";
        }
    }
    
    return 0;
}