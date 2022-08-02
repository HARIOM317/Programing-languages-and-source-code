#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    float x = 2;
    cout<<"Value of x is: "<<x<<endl;
    cout<<"Exponential Value of x is: "<<exp(x)<<endl;
    cout<<"Exponential value of x to the power minus one is: "<<expm1(x)<<endl;
    cout<<"base 2 exponential value of x is: "<<exp2(x)<<endl;
    cout<<"Natural log value of x is: "<<log(x)<<endl;
    cout<<"log of x is: "<<logb(x)<<endl;
    cout<<"commone log value of x is: "<<log10(x)<<endl;
    cout<<"Natural log value plus one of x is: "<<log1p(x)<<endl;
    cout<<"base 2 log of x is: "<<log2(x)<<endl;
    cout<<"Exponent value of x is: "<<ilogb(x)<<endl;

    return 0;
}