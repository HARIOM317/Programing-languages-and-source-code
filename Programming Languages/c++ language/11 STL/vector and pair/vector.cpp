#include <bits/stdc++.h>
// vector is dynamic array hence we can allocate it memory at runtime

using namespace std;

int main(){
    vector<int> v;
    v.push_back(11);
    v.push_back(207);
    v.push_back(3);
    v.push_back(44);
    v.push_back(15);

    cout<<"Elements of vector using for loop : "<<endl;
    // iterate vector using loop
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<endl;
    }
    
    // iterate vector using iterator
    cout << "\nElements of vector using iterator : " << endl;
    vector<int>::iterator iter;
    for(iter = v.begin(); iter!=v.end(); iter++){
        // iter is a pointer
        cout<<*iter<<endl;
    }

    // iterate vector using auto keyword
    cout << "\nElements of vector using auto keyword : " << endl;
    for(auto element:v){
        cout<<element<<endl;
    }

    // sort vector v
    sort(v.begin(), v.end());
    cout << "\nElements of vector v after sorting : " << endl;
    for (auto element : v)
    {
        cout << element << endl;
    }

    // creating a vector of 5 size with every element 50
    vector<int> v2(5, 50);

    // swapping v and v2
    swap(v, v2);

    cout << "\nElements after swapping of vector v : " << endl;
    for (auto element : v)
    {
        cout << element << endl;
    }
    cout << "Elements after swapping of vector v2 : " << endl;
    for (auto element : v2)
    {
        cout << element << endl;
    }

    return 0;
}