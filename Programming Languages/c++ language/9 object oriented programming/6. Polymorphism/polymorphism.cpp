#include <bits/stdc++.h>

using namespace std;

// class for function overloading
class FuncOverLoading
{
public:
    void fun()
    {
        cout << "I am a function with no argument" << endl;
    }
    // function overloading
    void fun(int x)
    {
        cout << "I am a function with int argument" << endl;
    }

    // function overloading
    void fun(double x)
    {
        cout << "I am a function with double argument" << endl;
    }
};

// class for operator overloading
class Complex
{
private:
    int real, imag;

public:
    // constructor
    Complex(int r=0, int i=0)
    {
        real = r;
        imag = i;
    }

    // operator overloading by reference
    Complex operator + (Complex const &obj)
    {
        Complex res;
        res.imag = imag + obj.imag;
        res.real = real + obj.real;
        return res;
    }

    void display()
    {
        cout << real <<" + "<< imag<<"i";
    }
};

// class for function overriding
// Base class
class base{
    public:
    virtual void print(){
        cout<<"This is the base class's print function"<<endl;
    }
    void display(){
        cout<<"This is the base class's display function"<<endl;
    }
};
// Derived class
class derived: public base{
    public:
    void print(){
        cout<<"This is the derived class's print function"<<endl;
    }
    void display(){
        cout<<"This is the derived class's display function"<<endl;
    }
};



int main()
{
    FuncOverLoading obj;
    // function overloading
    cout<<"\n\nFunction overloading\n";
    obj.fun();
    obj.fun(5);
    obj.fun(8.5);

    // operator overloading
    Complex c1(12, 7), c2(6, 7);
    Complex c3 = c1 + c2;
    cout << "\n\nOperator overloading\n";
    c3.display();

    // function overriding
    // creating pointer of base class
    base *basePtr;
    // creating derived class object
    derived d;
    basePtr = &d;
    cout << "\n\nFunction overriding\n";
    basePtr -> print();
    basePtr -> display();

    return 0;
}