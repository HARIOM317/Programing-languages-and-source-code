#include<iostream>
#include<math.h>

using namespace std;

int main()
{
  int n;
  cout<<"Enter a number"<<endl;
  cin>>n;
  int sum = 0;
  int originalnumber= n;
  while (n>0)
  {
      int lastdigit = n%10;
      sum+=pow(lastdigit,3);
      n = n/10;
  }
  if(sum==originalnumber){
      cout<<"ARMSTRONG NUMBER"<<endl;
  }
  else{
      cout<<"NOT A ARMSTRONG NUMBER"<<endl;
  }
    
    return 0;
}