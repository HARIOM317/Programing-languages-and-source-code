/*
Problem:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Note: Avoid duplicates

Sample test case:
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
*/

#include <bits/stdc++.h>

using namespace std;

void helper(vector<int> a, vector<vector<int>> &ans, int idx){
    if(idx == a.size()){
        ans.push_back(a);
        return;
    }
    for (int i = idx; i < a.size(); i++)
    {
        if(i != idx && a[i] == a[idx]){
            continue;
        }
        swap(a[i], a[idx]);
        helper(a, ans, idx+1);
    }
    
}

vector<vector<int>> permute(vector<int> nums){
    sort(nums.begin(), nums.end());
    vector<vector<int>> ans;
    helper(nums, ans, 0);
    return ans;
}

int main()
{
    int n;
    cout << "Enter size: ";
    cin >> n;

    vector<int> a(n);

    cout<<"Enter elements: \n";
    for(auto &i: a){
        cin>>i;
    }
    vector<vector<int>> res = permute(a);

    cout<<"\nAll possible unique permutations are: \n\n";
    for(auto v: res){
        for(auto i: v){
            cout<<i<<" ";
        }cout<<endl;
    }
    return 0;
}