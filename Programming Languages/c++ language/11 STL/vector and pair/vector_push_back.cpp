#include<iostream>
#include<vector>

using namespace std;

template <class T>
void display(vector<T> &v){
    cout<<"Displaying this vector ! "<<endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;   
}

int main()
{
    //Ways to creat a vector

    vector<int>vec1;  // Zero length integer vector
    // display(vec1);

    vector<char>vec2(4);  // 4-elements character vector
    //vec2.push_back('15');
    // display(vec2);

    vector<char>vec3(vec2); // 4-elements character vector from vec2
    // display(vec3);

    vector<int>v(6,3);  // 6 elements vector of 3s
    display(v);


    int element, size;

    // cout<<"Enter the size of the vector : ";
    // cin>>size;
    // for (int i = 0; i < size; i++)
    // {
    //     cout<<"Enter an element to add this vector : "<<endl;
    //     cin>>element;
    //     vec1.push_back(element);
    // }
    // vec1.pop_back();

    // display(vec1);
    // vector<int> :: iterator iter = vec1.begin();
    // vec1.insert(iter+1, 10,  578);          //vec1.insert(pointer, how many copy, which number);
    // display(vec1);

    return 0;
}