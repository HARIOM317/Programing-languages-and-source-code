#include <iostream>

using namespace std;

class A{
    // Empty class
    // class size = 1
};

class B{
    // property
    int size;   // size 4
};

class C{
    // properties
    int size;     // size 4
    char gender;  // size 4
    float height; // size 4
};
class D{
    // class size = 1
    public:
    // Behaviour (No size)
    void dance()
    {
        cout << "I can dance" << endl;
    }
    void play()
    {
        cout << "I can play" << endl;
    }
};
class E{
    // properties
    int size;   // size 4
    char gender;    // size 4
    char firstName[8];   // size 8
    char lastName[10];   // size 8
    float height;   // size 4
    float weight;   // size 4

public:
    // Behaviour (No size)
    void dance(){
        cout<<"I can dance"<<endl;
    }
    void play(){
        cout<<"I can play"<<endl;
    }
};

int main(){
    A a;
    B b;
    C c;
    D d;
    E e;
    cout<<"Size of empty class A : "<<sizeof(a)<<endl;
    cout<<"Size of class B with one variable : "<<sizeof(b)<<endl;
    cout<<"Size of class C with many variable : "<<sizeof(c)<<endl;
    cout<<"Size of class D with behaviour/methods : "<<sizeof(d)<<endl;
    cout<<"Size of class E with properties and behaviour : "<<sizeof(e)<<endl;

    return 0;
}