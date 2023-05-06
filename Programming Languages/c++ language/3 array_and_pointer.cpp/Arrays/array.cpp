#include<iostream>

using namespace std;

int main()
{
    int marks[] = {89,65,87,56,98,89,57,39,28,29};
    int mathmarks[5];
    mathmarks[0] = 57;
    mathmarks[1] = 67;
    mathmarks[2] = 98;
    mathmarks[3] = 74;
    mathmarks[4] = 87;
    int i=0;
    int j=0;
    cout<<"\nthe marks are:\n"<<endl;
    while (i<10)
    {
        cout<<"The marks of student "<<i<<" is "<<marks[i]<<endl;
        i++;
    }
    cout<<"\nThe mathmarks are:\n"<<endl;
    do
    {
        cout<<"the mathmarks of student "<<j<<" is "<<mathmarks[j]<<endl;
        j++;
    } while (j<5);
    
    
    return 0;
}