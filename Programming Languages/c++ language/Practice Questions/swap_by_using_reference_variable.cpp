#include<iostream>

using namespace std;

// void swapReferenceVar(int &x, int &y){
//     int temp = x;                        //this will be swap of both variables
//     x = y;
//     y = temp;
// }

int & swapReferenceVar(int &x, int &y){
    int temp = x;
    x = y;                                 //this will update value of a and also swap
    y = temp;
    return x;
}

// int main()
// {                //THIS IS FOR SWAPING OF A AND B.
//     int a = 4, b = 5;
//     cout<<"Before swaping: The value of a is "<<a<<" and the value of b is "<<b<<endl;
//     swapReferenceVar(a, b);
//     cout<<"After swaping: The value of a is "<<a<<" and the value of b is "<<b<<endl;
//     return 0;
// }

int main()
{                   //THIS IS FOR UPDATING OF VALUE A TO 45 AND ALSO SWAP THE VALUE OF B.
    int a = 4, b = 5;
    cout<<"Before swaping: The value of a is "<<a<<" and the value of b is "<<b<<endl;
    swapReferenceVar(a, b) = 45;
    cout<<"After swaping: The value of a is "<<a<<" and the value of b is "<<b<<endl;
    return 0;
}