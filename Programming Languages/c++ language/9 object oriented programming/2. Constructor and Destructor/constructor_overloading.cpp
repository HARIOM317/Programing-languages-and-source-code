#include<iostream>

using namespace std;

class complex{
    int a, b;
    public:
    complex(int x, int y){
        a = x;
        b = y;
    }
    complex(int x){
        a = x;
        b = 0; 
    }
    complex(){
        a = 0;
        b = 0;
    }
    void printNumber(){
        cout<<"Your complex number is: "<<a<<" + "<<b<<"i"<<endl;
    }
};

int main()
{
    cout<<"\nconstructor overloading :"<<endl;
    complex c1(4, 6);
    c1.printNumber();

    cout<<"\nconstructor overloading first :"<<endl;
    complex c2(7);
    c2.printNumber();

    cout<<"\nconstructor overloading second :"<<endl;
    complex c3;
    c3.printNumber();

    return 0;
}