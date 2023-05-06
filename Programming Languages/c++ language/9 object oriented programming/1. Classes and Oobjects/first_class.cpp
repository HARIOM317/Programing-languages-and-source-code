#include <iostream>

using namespace std;

class Student
{
    // by default private member
    string name;
public:
    int age;
    bool gender;

    // accessing name using setName method
    void setName(string s){
        name = s;
    }

    void printInfo()
    {
        cout << "Name = " << name << endl;
        cout << "Age = " << age << endl;
        cout << "Gender = " << gender << endl;
        cout << "\n\n";
    }
};

int main()
{
    // Creating an array of Student class
    Student arr[3];
    // taking details as input of all objects of class Student by user
    for (int i = 0; i < 3; i++)
    {
        string s;
        cout << "Enter name of student " << i << " : ";
        cin >> s;
        arr[i].setName(s);

        cout << "Enter age of student " << i << " : ";
        cin >> arr[i].age;

        cout << "Enter gender (1 for male and 0 for female) of student " << i << " : ";
        cin >> arr[i].gender;
        cout << "\n";
    }

    // printing student details
    for (int i = 0; i < 3; i++)
    {
        arr[i].printInfo();
    }

    return 0;
}