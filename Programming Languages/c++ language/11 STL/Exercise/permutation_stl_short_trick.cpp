#include <bits/stdc++.h>

using namespace std;
vector<vector<int>> ans;

int main(){
    cout << "Enter size: ";
    int n;
    cin >> n;
    vector<int> a(n);

    cout << "Enter elements: \n";
    for (auto &i : a)
    {
        cin >> i;
    }
    
    sort(a.begin(), a.end());
    do
    {
        ans.push_back(a);
    } while (next_permutation(a.begin(), a.end()));

    cout << "\nAll possible permutations are: \n\n";
    for (auto v : ans)
    {
        for (auto i : v)
        {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}