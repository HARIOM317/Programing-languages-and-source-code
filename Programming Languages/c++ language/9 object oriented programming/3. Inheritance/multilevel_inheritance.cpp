#include<iostream>

using namespace std;

class vehicle{
    public:
    vehicle(){
        cout<<"I have a vehicle."<<endl;
    }
};

class fourWheeler : public vehicle{
    public:
    fourWheeler(){
        cout<<"there are four wheels in my vehicle."<<endl;
    }
};

class car : protected fourWheeler{
    public:
    car(){
        cout<<"that is a car."<<endl;
    }
};

int main()
{
    car obj;
    return 0;
}