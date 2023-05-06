#include<iostream>

using namespace std;

int main()
{
    int num, n=1;
    cout<<"Enter a number for multiplication table"<<endl;
    cin>>num;
    cout<<"\n\n";
    do
    {
        cout<<num<<" X "<<n<<"  =  "<<n*num;
        cout<<"\n";
        n++;
    } while (n<=10);
    cout<<"\n\n*****************************************************\n\n";
    return 0;
}
