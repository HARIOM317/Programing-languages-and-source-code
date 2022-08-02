#include<iostream>
#include<map>
#include<string>

using namespace std;

int main()
{
    map<string , int>m;
    int n;
    cout<<"Enter value of n : ";
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        string s;
        cout<<"Enter string : "<<i+1<<"\t";
        cin>>s;
        m[s]++;
    }cout<<endl;
    cout<<"\nfrequency of given string in lexicographical order are as follow : "<<endl;
    for(auto pr : m){
        cout<<pr.first<<" "<<pr.second<<endl;
    }
    
    return 0;
}