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
    helloWorld obj;     // statically object created
    helloWorld *obj2 = new helloWorld;      // dynamically object created
    obj.display();
    obj2->display();
    delete obj2;        // manually call destructor for dynamic object
    return 0;
}