#include <iostream>
using namespace std;

class Point
{
private:
    int x;
    int y;
    const int z;

public:

    Point(int i = 0, int j = 0, int k = 0) : x(i), y(j), z(k)
    { // initializer list
        cout << "\nSetting value using initializer list" << endl;
    }

    int getX() { return x; }
    int getY() { return y; }
    int getZ() { return z; }
};

int main()
{
    Point t1(10, 15, 20);
    cout << "x = " << t1.getX() << endl;
    cout << "y = " << t1.getY() << endl;
    cout << "z = " << t1.getZ() << endl<<endl;
    return 0;
}