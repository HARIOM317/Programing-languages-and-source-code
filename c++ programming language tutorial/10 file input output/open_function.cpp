#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string str1;
    ofstream out;
    out.open("sample1.txt");
   
    out << "Hello friends : "<<endl;
    out << "My name is HSR"<<endl;
    out << "HSR = Hariom Singh Rajput"<<endl;
    out.close();

    string str2;
    ifstream in;
    in.open("sample1.txt");

    while (in.eof() == 0)
    {
        getline(in, str2);
        cout<<str2<<endl;
    }
    in.close();
    return 0;
}