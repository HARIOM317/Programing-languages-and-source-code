#include <iostream>
#include<cmath>

using namespace std;

class simple_calculator
{
public:
    int val1, val2;
    void wellcome1()
    {
        cout << "\n\nThis is the simple calculator \n\n";
    }
    void get_Value1()
    {
        cout << "Enter the value of first number" << endl;
        cin >> val1;
        cout << "Enter the value of second number" << endl;
        cin >> val2;
    }
    void display1()
    {
        int num;
        cout << "Which operation you want to perform: \n"
             << "Enter 1 for addition \n"
             << "Enter 2 for substraction \n"
             << "Enter 3 for multiplication \n"
             << "Enter 4 for division \n";
        cin >> num;
        switch (num)
        {
        case 1:
            cout << "Sum = " << val1 + val2 << endl;
            break;
        case 2:
            cout << "Substraction = " << val1 - val2 << endl;
            break;
        case 3:
            cout << "Multiplication = " << val1 * val2 << endl;
            break;
        case 4:
            cout << "Division = " << val1 / val2 << endl;
            break;

        default:
            break;
        }
    }
};

class scientific_calculator{
    int c;
    public:
     void wellcome2()
    {
        cout << "\n\nThis is the scientific calculator \n\n";
    }
    void getValue2(){
        cout<<"Enter a number:"<<endl;
        cin>>c;
    }
    void display2(){
        cout<<"The value of sin(a) is : "<<sin(c)<<endl;
        cout<<"The value of cos(a) is : "<<cos(c)<<endl;
        cout<<"The value of tan(a) is : "<<tan(c)<<endl;
        cout<<"The value of log(a) is : "<<log(c)<<endl;
    }
};

class hybrid_calculator : public simple_calculator, public scientific_calculator
{
public:
    hybrid_calculator()
    {
        cout << "\n\nWellcome to the hybrid calculator" << endl;
    }
};

int main()
{
    hybrid_calculator obj1;
    obj1.wellcome1();
    obj1.get_Value1();
    obj1.display1();
    hybrid_calculator obj2;
    obj2.wellcome2();
    obj2.getValue2();
    obj2.display2();
    return 0;
}