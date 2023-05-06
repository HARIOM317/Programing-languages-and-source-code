#include <iostream>
using namespace std;
class StaticMemberFunction
{
    // declare a static data member
    static int num;

public:
    // create static member function
    static int func()
    {
        return num;
    }
};
// initialize the static data member
int StaticMemberFunction ::num = 15;

int main()
{
    cout << "\nThe value of the static data member is: " << StaticMemberFunction::func() << endl;
    return 0;
}