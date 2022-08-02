#include <iostream>

using namespace std;

class employee
{
    int id;
    int static count;

public:
    void setdata(void)
    {
        cout << "Enter employee ID: ";
        cin >> id;
        count++;
    }
    void getdata(void)
    {
        cout << "The ID of this employee is " << id << " and this is employee number " << count << endl;
    }
    static void getcount(void)
    {
        cout << "The value of count is " << count << endl;
    }
};
int employee ::count = 100;
int main()
{
    employee hariom, abhishek, aman;

    hariom.setdata();
    hariom.getdata();
    employee::getcount();

    abhishek.setdata();
    abhishek.getdata();
    employee::getcount();

    aman.setdata();
    aman.getdata();
    employee::getcount();

    return 0;
}