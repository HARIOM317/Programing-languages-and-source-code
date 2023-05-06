#include<iostream>
#include<map>

using namespace std;

int main()
{
    map<int, string>m;

    m[1] = "hariom";
    m[5] = "welcome";
    m[7] = "back";
    m[3] = "rajput";
    m[8] = "in c++";
    m.insert({2, "singh"});

    cout<<"Before erasing: "<<endl;
    for(auto i : m){
        cout<<i.first<<" "<<i.second<<endl;
    }
    cout<<"Finding 3 -> "<<m.count(3)<<endl;

    m.erase(2);
    cout<<"After erasing: ";
    for(auto i : m){
        cout<<i.first<<" "<<i.second<<endl;
    }cout<<endl;

    auto it = m.find(7);
    for (auto i = it; i != m.end(); i++)
    {
        cout<<(*i).first<<endl;
    }

    return 0;
}