#include<iostream>

using namespace std;

inline float moneyReceived(int currentMoney, float factor = 1.04){
    return currentMoney*factor;
}

int main()
{
    int money = 100000;
    cout<<"If you have "<<money<<" Rs in your account then you will get "<<moneyReceived(money)<<" Rs. after 1 year"<<endl;
    cout<<"For VIP: If you have "<<money<<" Rs in your account then you will get "<<moneyReceived(money, 1.1)<<" Rs. after 1 year"<<endl;
    cout<<"For Former: If you have "<<money<<" Rs in your account then you will get "<<moneyReceived(money, 1.2)<<" Rs. after 1 year"<<endl;
    return 0;
}