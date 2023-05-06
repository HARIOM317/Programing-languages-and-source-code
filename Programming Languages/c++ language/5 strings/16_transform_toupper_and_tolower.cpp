#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    string str = "hariom mewada";
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    cout<<str<<endl;
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    cout<<str<<endl;
    return 0;
}