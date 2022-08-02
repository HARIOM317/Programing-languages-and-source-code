#include<iostream>
#include<string>

using namespace std;

int main()
{
    string s1 = "fam";
    string s2 = "ily";
    s1.append(s2);
    // s1 = s1+s2;                  //WE CAN ALSO APPEND WITHOUT USING APPEND FUNCTION BY DOING THIS.
    cout<<s1<<endl;

    //Access selected characters of string

    cout<<s1[0]<<endl;
    cout<<s1[4]<<endl;
    cout<<s1[5]<<endl;
    return 0;
}