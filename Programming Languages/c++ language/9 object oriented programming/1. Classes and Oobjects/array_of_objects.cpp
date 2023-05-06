#include<iostream>

using namespace std;

class employee{
    int id;
    int salary;
    public:
    void setId(void){
        salary = 50000;
        cout<<"Enter ID of employee "<<endl;
        cin>>id;
    }
    void getId(void){
        cout<<"The id of employee is : "<<id<<endl;
    }
    
};

int main()
{
    employee hsr[5];
    for (int i = 0; i < 5; i++)
    {
        hsr[i].setId();
        hsr[i].getId();
    }

    return 0;
}