#include<iostream>
#include<stack>

using namespace std;
//FILO-First In Last Out
int main()
{
    stack<string>hsr;
    hsr.push("Hariom");
    hsr.push("Singh");
    hsr.push("Rajput");
    cout<<"Top element is : "<<hsr.top()<<endl;
    hsr.pop();
    cout<<"Now top element is : "<<hsr.top()<<endl;
    cout<<"Size of stack = "<<hsr.size()<<endl;
    cout<<"Is it empty or not ? "<<hsr.empty()<<endl;
    return 0;
}