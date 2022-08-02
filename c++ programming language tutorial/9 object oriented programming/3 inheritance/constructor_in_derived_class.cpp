#include<iostream>

using namespace std;

class base1{
    int data1;
    public:
    base1(int i){
        data1 = i;
        cout<<"Base1 class constructor called !"<<endl;
    }
    void printData1(){
        cout<<"The value of data1 is : "<<data1<<endl;
    }
};

class base2{
    int data2;
    public:
    base2(int i){
        data2 = i;
        cout<<"Base2 class constructor called !"<<endl;
    }
    void printData2(){
        cout<<"The value of data2 is : "<<data2<<endl;
    }
};

class derived : public base1, virtual public base2{
    int derived1, derived2;
    public:
    derived(int a, int b, int c, int d) : base1(a), base2(b){
        derived1 = c;
        derived2 = d;
        cout<<"Derived class constructor called !"<<endl;
    }
    void printData3(){
        cout<<"The value of derived 1 is : "<<derived1<<endl;
        cout<<"The value of derived 2 is : "<<derived2<<endl;
    }
};

int main()
{
    derived hariom(10, 20, 30, 40);
    hariom.printData1();
    hariom.printData2();
    hariom.printData3();
    return 0;
}