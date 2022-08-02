#include <iostream>

using namespace std;

class employee
{
public:
    string name;
    int salary;

    employee(string n, int s)
    {
        this->name = n;
        this->salary = s;
    }
        void printDetaile()
        {
            cout << "the name of our first employee is " << this->name << " and his salary is " << this->salary << endl;
        }
};

int main()
{
    employee har("Hariom Rajput", 345500);
    har.printDetaile();
    // har.name = "hariom";
    // har.salary = 35000;;
    // cout<<"the name of our first employee is "<<har.name<<" and his salary is "<<har.salary<<endl;
    return 0;
}