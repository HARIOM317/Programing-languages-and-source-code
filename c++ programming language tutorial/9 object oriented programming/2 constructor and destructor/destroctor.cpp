#include<iostream>

using namespace std;

class helloWorld
{
public:
    void display(){
        cout<<"Hello world"<<endl;
    }
    helloWorld();
    ~helloWorld();
};

helloWorld::helloWorld()
{
    cout<<"Constructor is called"<<endl;
}

helloWorld::~helloWorld()
{
    cout<<"Destructor is called"<<endl;
}


int main()
{
    helloWorld obj;
    obj.display();
    return 0;
}