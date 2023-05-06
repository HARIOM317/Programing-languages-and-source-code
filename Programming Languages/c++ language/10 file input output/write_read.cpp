#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ofstream hariom("sample1.txt");
    string name;
    cout<<"Enter your name: ";
    cin>>name;
    hariom<<"My name is " + name;
    hariom.close();

    string str;
    ifstream HSR("sample1.txt");
    getline(HSR, str);
    cout<<"The content founds in sample1.txt is : "<<str;
    return 0;
}