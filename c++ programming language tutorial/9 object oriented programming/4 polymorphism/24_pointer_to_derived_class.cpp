#include<iostream>

using namespace std;

class baseClass{
    public:
    int var_base;
    void display(){
        cout<<"Base class variable is : "<<var_base<<endl;
    }
};

class derivedClass : public baseClass{
    public:
    int var_derived;
    void display(){
        cout<<"Derived class variable is : "<<var_derived<<endl;
    }
};

int main()
{
    baseClass * baseClass_pointer;
    baseClass obj_baseClass;
    derivedClass obj_derivedClass;
    baseClass_pointer = & obj_derivedClass;     //pointing base class pointer to derived class

    baseClass_pointer->var_base = 55;           
    // baseClass_pointer->derived_base = 55;    //it will throw an error
    baseClass_pointer->display();

    derivedClass * derivedClass_pointer;
    derivedClass_pointer =  & obj_derivedClass;

    derivedClass_pointer->var_derived = 155;
    derivedClass_pointer->display();

    return 0;
}