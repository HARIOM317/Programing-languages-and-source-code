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
    int code = ch;
    string ros = s.substr(1);

    sub_sequence(ros, ans);
    sub_sequence(ros, ans + ch);
    sub_sequence(ros, ans + to_string(code)); // converting int(code) to str(code).
}

int main()
{
    sub_sequence("AB", "");

    return 0;
}