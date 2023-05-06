#include<iostream>

using namespace std;

class complex
{
private:
    int a, b;
public:
    // parameterized constructor
    complex(int, int);
    void printNumber(){
        cout<<"Complex number is: "<<a<<" + "<<b<<"i"<<endl;
    }
};

complex::complex(int x, int y)
{
    a = x;
    b = y;
}

int main()
{
    //Implicit call
    complex c1(4, 8);

    //Explicit call
    complex b = complex(7, 9);

    c1.printNumber();
    b.printNumber();
    
    return 0;
}