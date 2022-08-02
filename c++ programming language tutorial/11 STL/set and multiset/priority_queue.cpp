#include <iostream>
#include <queue>

using namespace std;

int main()
{
    priority_queue<int> p;
    p.push(1);
    p.push(4);
    p.push(2);
    p.pop();
    cout << "After first pop" << endl;
    while (!p.empty())
    {
        cout << p.top() << endl;
        p.pop();
    }
    cout << "After second pop" << endl;
    p.push(3);
    p.push(8);
    p.pop();
    while (!p.empty())
    {
        cout << p.top() << endl;
        p.pop();
    }
    return 0;
}