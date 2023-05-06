#include <iostream>

using namespace std;

class Box
{
private:
    double length;
    double breadth;
    double height;
public:
    static int objectCount;

    Box(double l = 2.0, double b = 2.0, double h = 2.0)
    {
        cout << "Constructor called." << endl;
        length = l;
        breadth = b;
        height = h;

        // Increase every time object is created
        objectCount++;
    }

    double Volume()
    {
        return length * breadth * height;
    }
};

// Initialize static member of class Box
int Box::objectCount = 0;

int main(void)
{
    Box Box1(3.3, 1.2, 1.5);
    Box Box2(8.5, 6.0, 2.0);

    // Print total number of objects.
    cout << "Total objects: " << Box::objectCount << endl;
    cout<<"Volume of box 1 : "<<Box1.Volume()<<endl;
    cout<<"Volume of box 2 : "<<Box2.Volume()<<endl;

    return 0;
}