#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    string st1;
    ifstream read("sample1.txt");
    getline(read, st1);
    cout<<st1;
    return 0;
}