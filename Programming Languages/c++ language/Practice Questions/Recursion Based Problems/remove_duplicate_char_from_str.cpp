#include <iostream>

using namespace std;

string removeDuplicates(string str)
{
    if (str.length() == 0)
    {
        return "";
    }
    char ch = str[0];
    string ans = removeDuplicates(str.substr(1));
    if (ch == ans[0])
    {
        return ans;
    }

    return (ch + ans);
}

int main()
{
    cout << removeDuplicates("aaabbcddeefg");

    return 0;
}