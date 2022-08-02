#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> l;
    l.push_back(5);
    l.push_front(8);

    for (int i : l)
    { //i:l-> i belongs to l
        cout << i << " ";
    }
    cout << endl;

    l.erase(l.begin());
    cout << "After erase: ";
    for (int i : l)
    { //i:l-> i belongs to l
        cout << i << " ";
    }
    cout << endl;
    cout<<"Size = "<<l.size();
    return 0;
}