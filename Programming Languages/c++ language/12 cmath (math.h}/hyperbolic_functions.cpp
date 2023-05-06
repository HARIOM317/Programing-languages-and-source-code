#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    double degree;
    cout<<"Enter the value of degree ->  ";
    cin>>degree;
    double radian = degree*3.14/180;
    cout<<"Hyperbolic cosine of given angle is: "<<cosh(radian)<<endl;   
    cout<<"Hyperbolic sine of given angle is: "<<sinh(radian)<<endl;   
    cout<<"Hyperbolic tangent of given angle is: "<<tanh(radian)<<endl;   
    cout<<"Inverse of hyperbolic cosine is: "<<acosh(radian)<<endl;   
    cout<<"Inverse of hyperbolic sine is: "<<asinh(radian)<<endl;   
    cout<<"Inverse of hyperbolic tangent is: "<<atanh(radian)<<endl;   
    return 0;
}