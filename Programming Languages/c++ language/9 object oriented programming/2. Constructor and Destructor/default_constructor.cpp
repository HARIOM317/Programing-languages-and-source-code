#include<iostream>

using namespace std;

class complex{
    int a, b;
    public:

    // default constructor because no parameter is passing
    complex(void);          //constructor declaration

    void printNumber(){
        cout<<"Your complex number is: "<<a<<" + "<<b<<"i"<<endl;
    }
};
complex :: complex(void){           //constructor defintion
    a = 10, b = 20;
}
 
int main()
{
    complex c1, c2, c3;
    c1.printNumber();
    c2.printNumber();
    c3.printNumber();
    return 0;
}