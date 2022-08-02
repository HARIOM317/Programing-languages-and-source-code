#include <iostream>  
#include<list>  
using namespace std;  
int main()  
{  
   list<int> li={6,4,10,2,4,1};  
   list<int>:: iterator itr;  
   cout<<"Elements of list are : ";  
   for(itr=li.begin();itr!=li.end();++itr)  
   std::cout << *itr<<",";  
   li.sort();  
   cout<<'\n';  
   cout<<"Sorted elements are : ";  
   for(itr=li.begin();itr!=li.end();++itr)  
   std::cout << *itr <<",";  
    return 0;  
}  