#include <iostream>

using namespace std;

class A{
    public:
    void greet(){
        cout<<"Good Morning friends!"<<endl;
    }
};

class B{
    public:
    void greet(){
        cout<<"Good Afternoon friends!"<<endl;
    }
};

class C : public A, public B{
    public:
    void show(){
        cout<<"greet() function throws an ambiguity error!"<<endl;
    }
};

int main(){
    C c1;
    // c1.greet(); // ambiguity error
    c1.show();

    // resolving ambiguity
    c1.A::greet();
    c1.B::greet();

    return 0;
}