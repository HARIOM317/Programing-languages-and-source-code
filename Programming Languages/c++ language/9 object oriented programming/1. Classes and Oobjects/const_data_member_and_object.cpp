#include <iostream>
using namespace std;

class ABC
{
public:
    const int A;
    ABC(int y) : A(y)
    {
        cout << " The value of y: " << y << endl;
    }
};
int main()
{
    ABC obj(10);
    // cout << " The value of constant data member 'A' is: " << obj.A << endl;
    // obj.A = 5; // it shows an error.

    const ABC obj2(20);
    // cout<<"The value of A is : "<<obj2.A<<endl;
    return 0;
}