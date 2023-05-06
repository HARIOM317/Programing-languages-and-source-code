#include<iostream>
#include<queue>

using namespace std;

int main()
{
    queue<string>hsr;
    hsr.push("Hariom");
    hsr.push("Singh");
    hsr.push("Rajput");
    cout<<"First element is: "<<hsr.front()<<endl;
    cout<<"last element is: "<<hsr.back()<<endl;
    hsr.pop();
    cout<<"Now first element is: "<<hsr.front()<<endl;
    cout<<"Size of queue = "<<hsr.size()<<endl;
    cout<<"Empty or not = "<<hsr.empty()<<endl;

    return 0;
}