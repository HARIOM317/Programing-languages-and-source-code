#include<iostream>

using namespace std;

class base{                         //Abstract class
    public:
    virtual void display() = 0;     //pure virtual function
};

class derived : public base{
    public:
    void display(){
        cout<<"This is the display function of derived class"<<endl;
    }
};

int main()
{
    base * ptr;
    derived obj;
    ptr = & obj;
    ptr->display();  
    return 0;
}