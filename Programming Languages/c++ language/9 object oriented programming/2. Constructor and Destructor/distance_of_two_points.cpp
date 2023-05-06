#include<iostream>
#include<cmath>

using namespace std;

class dist{
    int x, y;
    public:
    dist(int a, int b){
        x = a;
        y = b;
    }
    void display(){
        cout<<"The point is("<<x<<", "<<y<<")"<<endl;
    }
    friend double answer(dist, dist);
};
double answer(dist p1, dist p2){
    double result = sqrt(pow(p1.x-p2.x , 2)+pow(p1.y-p2.y, 2));
    return result;
}
int main()
{
    dist p(5,7);
    p.display();
    dist q(7,10);
    q.display();
    double res = answer(p, q);
    cout<<"The distance is: "<<res<<endl;
    return 0;
}