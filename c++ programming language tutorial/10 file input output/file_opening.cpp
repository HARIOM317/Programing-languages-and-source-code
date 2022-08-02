#include<iostream>
#include <fstream>
using namespace std;
int main()
{
fstream new_file; 
new_file.open("new",ios::out);  
if(!new_file) 
{
cout<<"File creation failed";
}
else
{
cout<<"New file created";
}
new_file.close();
return 0;
}