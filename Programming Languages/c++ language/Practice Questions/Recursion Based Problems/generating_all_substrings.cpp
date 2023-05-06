#include <iostream>

using namespace std;

void sub_sequence(string s, string ans)
{
    if (s.length() == 0)
    {
        cout << ans << endl;
        return;
    }

    char ch = s[0];
    string ros = s.substr(1);

    sub_sequence(ros, ans);
    sub_sequence(ros, ans + ch);
}

int main()
{
    sub_sequence("ABC", "");

    return 0;
}