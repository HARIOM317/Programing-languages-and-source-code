#include<iostream>

using namespace std;

class shop{
    char item;
    float price;
    public:
    void setData(char a, float b){
        item = a;
        price = b;
    }
    void getData(void){
        cout<<"The item name is : "<<item<<endl;
        cout<<"The item price is: "<<price<<endl;
    }
};

int main()
{
    int size = 4;
    shop * ptr = new shop[size];  
    shop * ptrTemp = ptr;
    int i;
    char p;
    float q;
    for (i = 0; i < size; i++)
    {
        cout<<"Enter name and price of item: "<<i+1<<endl;
        cin>>p>>q;
        ptr->setData(p, q);
        ptr++;
    }
    for (i = 0; i < size; i++)
    {
        cout<<"Item number : "<<i+1<<endl;
        ptrTemp->getData();
        ptrTemp++;
    }
    
    return 0;
}
