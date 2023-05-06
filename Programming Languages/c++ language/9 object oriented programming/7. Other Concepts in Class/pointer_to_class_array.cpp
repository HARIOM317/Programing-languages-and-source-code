#include <iostream>

using namespace std;

class Rectangle
{
private:
    int length, breadth;

public:
    void setData(int l, int b){
        length = l;
        breadth = b;
    }
    int getArea()
    {
        return 2 * length * breadth;
    }
};

int main()
{
    Rectangle var[2];   // array of object
    var[0].setData(5, 6);
    var[1].setData(3, 4);
    Rectangle *ptr;
    ptr = var;

    for (int i = 0; i < 2; i++)
    {
        cout<<"Area of Rectangle"<<(i+1)<<" is : "<<(ptr+i)->getArea()<<endl;
    }

    return 0;
}