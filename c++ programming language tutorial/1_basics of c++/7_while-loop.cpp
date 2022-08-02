#include <iostream>

using namespace std;

int main()
{
    int num;
    int i = 2;
    cout<<"\n\n***Program for first n even numbers***\n\n";
    cout<<"enter a number"<<endl;
    cin>>num;
    while (i <= 2*num)
    {
        if (i % 2 == 0)
        {
            cout << i;
            cout << "\t";
        }
        i++;
    }

    return 0;
}