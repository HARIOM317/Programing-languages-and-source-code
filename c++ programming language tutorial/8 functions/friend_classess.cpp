#include<iostream>

using namespace std;

class complex;                  //Forward declaration

class calculator{
    public:
    int add(int a, int b){
        return a+b;
    }
    int sumrealComplex(complex, complex);
    int sumCompComplex(complex, complex);
};

class complex{
    int a, b;
    // friend  int calculator :: sumrealComplex(complex, complex);    //we can make friends of all fuction of other class (This is first way)
    // friend  int calculator :: sumCompComplex(complex, complex);    //we can make friend of the class (This is orther way)
    friend class calculator;
    public:
    void setNumber(int n1, int n2){
        a = n1;
        b = n2;
    }
    void printNumber(){
        cout<<"Complex number is: "<<a<<" + "<<b<<"i"<<endl;
    }
};

int calculator :: sumrealComplex(complex o1, complex o2){
    return (o1.a + o2.a);
}
int calculator :: sumCompComplex(complex o1, complex o2){
    return (o1.b + o2.b);
}

int main()
{
    complex o1, o2;
    o1.setNumber(5, 7);
    o2.setNumber(6, 8);
    calculator calc;
    int res = calc.sumrealComplex(o1, o2);
    cout<<"The sum of real part of o1 and o2 is: "<<res<<endl;
    int resc = calc.sumCompComplex(o1, o2);
    cout<<"The sum of complex part of o1 and o2 is: "<<resc<<endl;
    return 0;
}