#include <iostream>

using namespace std;

class Rectangle{
    private:
    int length, breadth;
    public:
    Rectangle(int l, int b){
        length = l;
        breadth = b;
    }
    int getArea(){
        return 2*length*breadth;
    }
};

int main(){
    Rectangle var1(5, 3);
    Rectangle *ptr = &var1;     // pointer object
    int area = ptr->getArea();
    cout<<"Area of Rectangle : "<<area<<endl;

    return 0;
}