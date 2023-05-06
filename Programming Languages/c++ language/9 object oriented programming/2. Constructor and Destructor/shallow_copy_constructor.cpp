#include <iostream>
using namespace std;
class Test
{
public:
    int a;
    int *p;
    Test(int x)
    {
        a = x;
        p = new int[a];
    }
    Test(Test &t)
    {
        a = t.a;
        p = t.p;
    }
};
int main()
{
    Test t1(5);
    t1.p[0] = 1;
    cout << "t1: " << t1.a << " " << t1.p[0] << endl;

    Test t2(t1);
    t2.p[0] = 10;
    cout << "t2: " << t2.a << " " << t2.p[0] << endl;

    cout << "t1: " << t1.a << " " << t1.p[0] << endl;

    return 0;
}