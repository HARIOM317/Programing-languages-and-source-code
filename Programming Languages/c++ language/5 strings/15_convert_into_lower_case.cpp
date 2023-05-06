#include<iostream>

using namespace std;

int main()
{
    string str = "HARIOM";
    for (int i = 0; i < str.size(); i++)
    {
        if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += 32;
        }
    }
    cout<<str<<endl;
    
    return 0;
}