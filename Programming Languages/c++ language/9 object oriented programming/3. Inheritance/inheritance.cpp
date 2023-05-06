#include<iostream>

using namespace std;

class vehicle{
    public:
    vehicle(){
        cout<<"This is a vehicle."<<endl;
    }
};

class fourWheeler : public vehicle{
    public:
    fourWheeler(){
        cout<<"This is also a four wheeler."<<endl;
    }
};

int main()
{
    fourWheeler obj;  
    return 0;
}