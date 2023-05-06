#include<iostream>

using namespace std;

template <class T>
class hariom{
    public:
    T data;
    hariom(T a){
        data = a;
    }
        void display();
};
template <class T>
void hariom<T>::display(){
    cout<<"Your data is : "<<data<<endl;
}

int main()
{
    hariom <int>obj(45);
    obj.display();
    return 0;
}