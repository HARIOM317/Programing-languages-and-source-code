#include <bits/stdc++.h>

using namespace std;

/*
problem: you have to given an array and you have to reduce it.

Input:
10  16  7   14  5   3   12  9

Output:
4   7   2   6   1   0   5   3

procedure to solve it:
step 1: (given array)
data    10  16  7   14  5   3   12  9
index   0   1   2   3   4   5   6   7

step 2: (sort with it's original index)
data    3   5   7   9   10  12  14  16
index   5   4   2   7   0   6   3   1

step 3: (put value from 0 to n on array's according to it's original index)
on index 5 -> 0
on index 4 -> 1
on index 2 -> 2
on index 7 -> 3
on index 0 -> 4
on index 6 -> 5
on index 3 -> 6
on index 1 -> 7

data    4   7   2   6   1  0  5  3
index   0   1   2   3   4   5   6   7

*/

bool myCompare(pair<int, int> p1, pair<int, int> p2){
    // return which element is less
    return p1.first < p2.first;
}

int main(){
    int arr[] = {10, 16, 7, 14, 5, 3, 12, 9};

    // print original array
    cout << "\nOriginal array:\n";
    for (int i = 0; i < 8; i++)
    {
        cout << arr[i] << "    ";
    }

    // creating vector v of type pair of int and int
    vector<pair<int, int>> v;

    for (int i = 0; i < (sizeof(arr)/sizeof(arr[0])); i++)
    {
        // Creating a pair using make_pair function and push_back it in vector v
        v.push_back(make_pair(arr[i], i));
    }
    
    // sorting array on it's default index.
    sort(v.begin(), v.end(), myCompare);

    // reducing array
    for (int i = 0; i < v.size(); i++)
    {
        // v[i].second is giving index
        arr[v[i].second] = i;
    }
    
    // print reduce array
    cout << "\nReduce array:\n";
    for (int i = 0; i < v.size(); i++)
    {
        cout<<arr[i]<<"    ";
    }
    
    return 0;
}