#include<iostream>

using namespace std;

class base1{
    protected:
    int val1;
    public:
    void set_val1(int a){
        val1 = a;
    }
};

class base2{
    protected:
    int val2;
    public:
    void set_val2(int a){
        val2 = a;
    }
};

class base3{
    protected:
    int val3;
    public:
    void set_val3(int a){
        val3 = a;
    }
};

class derived : public base1, public base2, public base3{
    public:
    void show(){
        cout<<"The value of base1 is: "<<val1<<endl;
        cout<<"The value of base2 is: "<<val2<<endl;
        cout<<"The value of base3 is: "<<val3<<endl;
        cout<<"The sum of these values is: "<<val1 + val2 + val3<<endl;
    }
};

int main()
{
    derived hariom;
    hariom.set_val1(125);
    hariom.set_val2(75);
    hariom.set_val3(100);
    hariom.show();
    return 0;
}