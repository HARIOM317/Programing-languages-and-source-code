#include<iostream>
#include<set>

using namespace std;

int main()
{
  multiset<int, greater<int>> set_1;

  set_1.insert(502);
  set_1.insert(502);
  set_1.insert(506);
  set_1.insert(507);
  set_1.insert(555);

  multiset<int, greater<int>>::iterator iterator_1;
  cout << "\nThe multiset elements are: ";
  for (iterator_1 = set_1.begin(); iterator_1 != set_1.end(); ++iterator_1)
  {
    cout << "\t" << *iterator_1;
  }
}