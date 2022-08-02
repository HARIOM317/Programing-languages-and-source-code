#include<iostream>
#include<map>
#include<string>

using namespace std;

int main()
{
    map<string, int>marksMap;
    marksMap["hariom"] = 99;
    marksMap["abhishek"] = 97;
    marksMap["shubham"] = 75;
    marksMap["aman"] = 54;
    marksMap["rohit"] = 23;
    marksMap.insert({{"ajay", 87}, {"rahul", 66}});
    map<string,int>::iterator iter;
    for(iter = marksMap.begin(); iter!=marksMap.end(); iter++){
        cout<<(*iter).first<<" "<<(*iter).second<<endl;
    }
    return 0;
}