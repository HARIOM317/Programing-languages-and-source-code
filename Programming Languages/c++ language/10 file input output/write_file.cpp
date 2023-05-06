#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    string st = "Hariom Singh Rajput";
    ofstream write("sample2.txt");
    write<<st;
    return 0;
}