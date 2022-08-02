#include<iostream>

using namespace std;

class vehicle{
    public:
    vehicle(){
        cout<<"This is a vehicle class"<<endl;
    }
};

class car : public vehicle{
    public:
    car(){
        cout<<"This is a car"<<endl;
    }
};

class bus : public vehicle{
    public:
    bus(){
        cout<<"This is a bus"<<endl;
    }
};

int main()
{
    car obj1;
    bus obj2;  
    return 0;
}