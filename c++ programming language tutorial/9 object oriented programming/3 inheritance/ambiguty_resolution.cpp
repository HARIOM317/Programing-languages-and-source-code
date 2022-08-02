#include<iostream>

using namespace std;

class base1{
    public:
    void greet(){
        cout<<"How are you?"<<endl;
    }
};

class base2{
    public:
    void greet(){
        cout<<"Kaise ho Aap?"<<endl;
    }
};

class derived : public base1, public base2{
    int a;
    public:
    void greet(){
        base1 :: greet();
    }
};

class B{
    public:
    void say(){
        cout<<"hello world"<<endl;
    }
};

class D : public B{
    public:
    void say(){
        cout<<"Hello friends"<<endl;
    }
};

int main()
{
    base1 obj1;
    base2 obj2;
    derived obj3;
    obj1.greet();
    obj2.greet();
    obj3.greet(); 
    D obj;
    obj.say(); 
    return 0;
}