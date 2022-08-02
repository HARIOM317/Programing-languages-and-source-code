#include <iostream>

using namespace std;

class A
{
public:
    int a;
};
class B : public A
{
public:
    int b;
};

class C : public A
{
public:
    int c;
};

class D : public B, public C
{
public:
    int d;
};
int main()
{
    D obj;
    obj.B::a = 10;
    obj.C::a = 100;
    obj.b = 150;
    obj.c = 200;
    obj.d = 50;
    cout << "\na from class B : " << obj.B::a << endl;
    cout << "a from class C: " << obj.C::a << endl;

    cout << "The value of b is : " << obj.b << endl;
    cout << "The value of c is : " << obj.c << endl;
    cout << "The value of d is : " << obj.d << endl;

    return 0;
}