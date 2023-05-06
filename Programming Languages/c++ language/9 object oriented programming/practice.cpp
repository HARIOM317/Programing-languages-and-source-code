#include <iostream>

using namespace std;

class StaticMemberFunction{
    static string name;
    public:
    static string getName(){
        return name;
    }
};

string StaticMemberFunction:: name = "hariom Singh rajput";

int main(){
    cout<<StaticMemberFunction::getName();

    return 0;
}