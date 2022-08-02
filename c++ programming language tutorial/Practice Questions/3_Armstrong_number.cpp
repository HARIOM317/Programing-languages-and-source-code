#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    int n;
    cout<<"Enter a n number: ";
    cin>>n;
    int num = 0;
    int originaln = n;
    while (n > 0)
    {
        int lastDigit = n%10;
        num = num + pow(lastDigit, 3);
        n = n/10;
    }
    if (num == originaln)
    {
        cout<<"Armstrong Number";
    }
    else{
        cout<<"Not a Armstrong number";
    }
    return 0;
}