#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    float x = 9.55;
    float y = -13.3;
    cout<<"Initial value of x and y is: "<<x<<", "<<y<<endl;
    cout<<"Round up value of x is: "<<ceil(x)<<endl;
    cout<<"Round down value of x is: "<<floor(x)<<endl;
    cout<<"Round off value of x is: "<<round(x)<<endl;
    cout<<"Rounded value of x and y is: "<<lround(x)<<", "<<lround(y)<<endl;
    cout<<"Rounded value of y is: "<<llround(y)<<endl;
    cout<<"Truncated value of x is: "<<trunc(x)<<endl;
    cout<<"Rounding to nearby,value is: "<<nearbyint(x)<<endl;

    return 0;
}