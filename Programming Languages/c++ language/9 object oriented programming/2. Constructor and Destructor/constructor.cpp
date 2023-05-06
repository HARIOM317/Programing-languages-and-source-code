#include <iostream>

using namespace std;

class Student{
    string name;

    public:
    int age;
    bool gender;

    // Default constructor
    Student(){
        cout<<"\nDefault constructor"<<endl;
    }

    // Parameterized constructor
    Student(string s, int a, int g){
        cout<<"\nParameterized constructor"<<endl;
        name = s;
        age = a;
        gender = g;
    }

    // copy constructor
    Student(Student &a){
        cout << "\nCopy constructor" << endl;
        name = a.name;
        age = a.age;
        gender = a.gender;
    }

    void setName(string s){
        name = s;
    }

    void getName(){
        cout<<"name = "<<name<<endl;
    }

    void printInfo(){
        cout<<"Name = "<<name<<endl;
        cout<<"Age = "<<age<<endl;
        cout<<"Gender = "<<gender<<endl;
    }
};

int main(){
    // call parameterized constructor
    Student a("Hariom", 20, 1);
    a.printInfo();

    // call default constructor
    Student b;
    // b.printInfo();       // return garbage values

    // call copy constructor
    Student c = a;   // copying all values of a in c
    c.printInfo();

    return 0;
}