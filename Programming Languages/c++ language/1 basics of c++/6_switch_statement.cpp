#include <iostream>

using namespace std;

int main()
{
    char choice;
    cout << "Choose your favorite color :\n 'p' for pink\n 'r' for red\n 'y' for yellow\n 'n' for non of these " << endl;
    cin >> choice;
    switch (choice)
    {
    case 'p':
        cout << "Your favorite color is pink" << endl;
        break;

    case 'r':
        cout << "Your favorite color is red" << endl;
        break;

    case 'y':
        cout << "Your favorite color is yellow" << endl;
        break;

    case 'n':
        cout << "You don't like any color " << endl;
        break;

    default:
        cout << "thank you";
        break;
    }
    return 0;
}