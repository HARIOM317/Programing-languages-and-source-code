#include <iostream>
using namespace std;

class Test
{
private:
    int x;
    int y;

public:
    Test(){
        this->x = 10;
        this->y = 20;
    }
    Test(int x, int y)
    {
        this->x = x;
        this->y = y;
    }
    Test setX(int a)
    {
        x = a;
        return *this;
    }
    Test setY(int b)
    {
        y = b;
        return *this;
    }
    void print() {
        cout << "x = " << x << " y = " << y << endl;
    }
};

int main()
{
    Test obj1;
    obj1.print();

    Test obj2(15,25);
    obj2.print();

    Test obj3;
    obj3.setX(100);
    obj3.setY(200);
    obj3.print();
    
    return 0;
}