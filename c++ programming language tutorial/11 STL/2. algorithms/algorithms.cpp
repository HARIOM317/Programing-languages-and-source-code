#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    vector<int> v;
    v.push_back(1);
    v.push_back(3);
    v.push_back(4);
    v.push_back(6);
    v.push_back(8);
    cout << "Finding 6 -> " << binary_search(v.begin(), v.end(), 6)<<endl;

    cout << "Upper bound : " << upper_bound(v.begin(), v.end(), 4) - v.begin() << endl;
    cout << "Lower bound : " << lower_bound(v.begin(), v.end(), 4) - v.begin() << endl;

    int a = 3;
    int b = 5;
    cout << "max = " << max(a, b) << endl;
    cout << "min = " << min(a, b) << endl;

    cout << "After swaping: " << endl;
    swap(a, b);
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    string abcd = "ABCD";
    cout << "Before reversing string is : " << abcd << endl;
    reverse(abcd.begin(), abcd.end());
    cout << "After reversing string is : " << abcd << endl<<endl;

    cout<<"Before rotate : ";
    for(int i:v){
        cout<<i<<" ";
    }cout<<endl;
    
    rotate(v.begin(), v.begin()+1, v.end());
    cout<<"After rotate : ";
    for(int i:v){
        cout<<i<<" ";
    }

    return 0;
}