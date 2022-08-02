#include<iostream>
#include<set>

using namespace std;

int main()
{
    set<int>s1;
    s1.insert(7);
    s1.insert(9);
    s1.insert(3);
    s1.insert(7);
    s1.insert(8);
    s1.insert(1);
    s1.insert(8);
    s1.insert(3);
    for(auto i:s1){
        cout<<i<<endl;
    }cout<<endl;

    set<int> :: iterator it = s1.begin();
    it++;
    s1.erase(it);
    for(auto i:s1){
        cout<<i<<endl;
    }cout<<endl;

    cout<<"9 is present or not -> "<<s1.count(9)<<endl;

    set<int> :: iterator itr = s1.find(7);
    for(auto it = itr; it!=s1.end(); it++){
        cout<<*it<<" ";
    }cout<<endl;

    return 0;
}