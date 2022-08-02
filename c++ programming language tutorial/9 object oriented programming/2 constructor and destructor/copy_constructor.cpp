#include<iostream>

using namespace std;

class number{
    int a;
    public:
    // number(){
    //     a = 0;
    // }
    number(int num){
        a = num;
    }
    number(number &obj){
        cout<<"Copy constructor called !"<<endl;
        a = obj.a;
    }
    void display(){
        cout<<"Number for this object is: "<<a<<endl;
    }
};

int main()
{
    number x(12), y(7), z(78);
    x.display();
    y.display();
    z.display();
    number z1(x);
    z1.display();
    number z2 = y;
    z2.display();
    return 0;
}