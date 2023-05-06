#include<iostream>

using namespace std;

int main()
{
    int a;
    cout<<"Enter your age"<<endl;
    cin>>a;
    if (a<18)
    {
        cout<<"you are not ready for COVID vacsination , please be pations"<<endl;
    }
    else{
        cout<<"you are ready for COVID vacsination"<<endl;
    }
    
    return 0;
}