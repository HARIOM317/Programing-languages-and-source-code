/*
Permutations: A permutation is a rearrangement of members of a sequence into a new sequence.
*/

/*
Problem:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Sample test case:
Input: nums = [1,2,3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
*/

#include <bits/stdc++.h>

using namespace std;
vector<vector<int>> ans;

void permute(vector<int> &a, int idx){
    if (idx == a.size()){
        ans.push_back(a);
        return;
    }
    for(int i=idx; i<a.size(); i++){
        swap(a[i], a[idx]);
        permute(a, idx+1);
        swap(a[i], a[idx]);
    }
    return;
}

int main(){
    cout<<"Enter size: ";
    int n;
    cin>>n;
    vector<int> a(n);

    cout<<"Enter elements: \n";
    for(auto &i : a){
        cin>>i;
    }
    permute(a, 0);
    
    cout<<"\nAll possible permutations are: \n\n";
    for(auto v: ans){
        for(auto i : v){
            cout<<i<<" ";
        }cout<<endl;
    }

    return 0;
}