#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<char> v{'C', '+', '#'};
    v.erase(v.begin() + 1);
    for (int i = 0; i < v.size(); i++)
        cout << v[i];
    cout << endl;

    vector<string> fruit{"mango", "apple", "strawberry", "kiwi", "banana"};
    cout << "fruit names are :";
    for (int i = 0; i < fruit.size(); i++)
        cout << fruit[i] << " ";
    cout << '\n';
    fruit.erase(fruit.begin() + 1, fruit.begin() + 3);
    cout << "After removing apple and strawbery fruits," << '\n';
    for (int i = 0; i < fruit.size(); i++)
        cout << fruit[i] << " ";
    return 0;
}