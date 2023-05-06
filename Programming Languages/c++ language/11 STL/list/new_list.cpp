#include <iostream>
#include <list>
using namespace std;
int main()
{
    list<int> li = {1, 2, 3, 4};
    list<int>::iterator itr = li.begin();
    li.insert(itr, 5);
    for (itr = li.begin(); itr != li.end(); ++itr){
        cout << *itr<<" ";
    }cout<<endl;

    list<string> li1 = {"C is a language"};
    list<string>::iterator itr1 = li1.begin();
    li1.insert(itr1, 2, "java ");
    for (itr1 = li1.begin(); itr1 != li1.end(); ++itr1){
        cout << *itr1;
    }cout<<endl;

    list<int> li2 = {1, 2, 3, 4, 5};
    list<int> li3 = {6, 7, 8, 9};
    list<int>::iterator itr3 = li2.begin();
    li2.insert(itr3, li3.begin(), li3.end());
    for (itr3 = li2.begin(); itr3 != li2.end(); ++itr3)
    {
        cout << *itr3<<" ";
        // cout << ? ? ;
    }cout<<endl;
    return 0;
}