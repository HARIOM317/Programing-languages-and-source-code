#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    double degree = 90;
    double radian = degree*3.14/180;
    cout<<"sine of an angle is: "<<sin(radian)<<endl;
    cout<<"cosine of an angle is: "<<cos(radian)<<endl;
    cout<<"tangent of an angle is: "<<tan(radian)<<endl;
    cout<<"Inverse of cosine is: "<<acos(radian)<<endl;
    cout<<"Inverse of sine is: "<<asin(radian)<<endl;
    cout<<"Inverse of tangent is: "<<atan(radian)<<endl;
    double x, y, result;
    x = -10.0;
    y = 10.0;
    result = atan2(y,x)*180/3.14;
    cout<<"the arc tangent for x = "<<x<<", y = "<<y<<" is: "<<result<<endl;
    return 0;
}