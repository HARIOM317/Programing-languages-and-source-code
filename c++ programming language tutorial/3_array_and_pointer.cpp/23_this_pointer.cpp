#include<iostream>

using namespace std;

class A{
    int a;
    public:
    // void setData(int a){     //first way
    //     this->a = a;
    // }
    A & setData(int a){         //second way
        this->a = a;
        return * this;
    }
    void getData(void){
        cout<<"The value of a is : "<<a<<endl;
    }
};

int main()
{
    A a;
    a.setData(1250).getData();          //second way
    a.getData();                     //first way
    return 0;
}