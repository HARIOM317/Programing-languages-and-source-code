#include<iostream>

using namespace std;

int main()
{
    int age;
    cout<<"Enter your age"<<endl;
    cin>>age;
    if(age<18 && age>0){
        cout<<"you are not ready for voting"<<endl;
    }
    else if(age==18){
        cout<<"You are ready for your first vote"<<endl;
    }
    else if (age>18){
        cout<<"You can vote"<<endl;
    }
    else{
        cout<<"Invalid age!"<<endl;
    }
    return 0;
}