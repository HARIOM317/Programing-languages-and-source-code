#include<iostream>

using namespace std;

int sum(int a, int b){
    cout<<"using function with 2 arguments "<<endl;
    return a+b;
}
int sum(int a, int b, int c){
    cout<<"using function with 3 arguments "<<endl;
    return a+b+c;
}

int main()
{
    cout<<"The sum of 3 and 6 is "<<sum(3,6)<<endl;
    cout<<"The sum of 3, 7 and 6 is "<<sum(3,7,6)<<endl;
    return 0;
}