#include<iostream>

using namespace std;
class y;

class x{
    int val1;
    friend void exchange(x &, y &);
    public:
    void inData(int a){
        val1 = a;
    }
    void display(void){
        cout<<val1<<endl;
    }
};

class y{
    int val2;
    friend void exchange(x &, y &);
    public:
    void inData(int a){
        val2 = a;
    }
    void display(void){
        cout<<val2<<endl;
    }
};
void exchange(x &a, y &b){
    int temp = a.val1;
    a. val1 = b.val2;
    b.val2 = temp;
}
int main()
{
    x oc1;
    y oc2;
    oc1.inData(45);
    oc2.inData(55);
    exchange(oc1,oc2);
    cout<<"The value of function 1 after swaping is: "<<endl;
    oc1.display();
    cout<<"The value of function 2 after swaping is: "<<endl;
    oc2.display();
    return 0;
}