#include<iostream>
#include<queue>

using namespace std;

int main()
{
    priority_queue<int>maxi; //Maximum queue
    priority_queue<int,vector<int>,greater<int>>mini; //Minimum queue
    maxi.push(5);
    maxi.push(9);
    maxi.push(7);
    maxi.push(1);
    maxi.push(12);
    maxi.push(4);
    maxi.push(8);
    cout<<"Size = "<<maxi.size()<<endl;
    int n = maxi.size();
    for (int i = 0; i < n; i++)
    {
        cout<<maxi.top()<<"  "<<endl;
        maxi.pop();
    }cout<<endl;
    cout<<"Maxi is empty or not? -> "<<maxi.empty()<<endl;

    mini.push(5);
    mini.push(9);
    mini.push(7);
    mini.push(1);
    mini.push(12);
    mini.push(4);
    mini.push(8);
    cout<<"Size = "<<mini.size()<<endl;
    int m = mini.size();
    for (int i = 0; i < m; i++)
    {
        cout<<mini.top()<<"  "<<endl;
        mini.pop();
    }cout<<endl;
    cout<<"Mini is empty or not? -> "<<mini.empty()<<endl;

    return 0;
}