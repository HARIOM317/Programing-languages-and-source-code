#include <iostream>

using namespace std;

class student
{
protected:
    int roll_Number;

public:
    void set_number(int a)
    {
        roll_Number = a;
    }
    void print_number(void)
    {
        cout << "Your roll number is: " << roll_Number << endl;
    }
};

class test : virtual public student
{
protected:
    float maths, physics, chemistry;

public:
    void set_marks(float m1, float m2, float m3)
    {
        maths = m1;
        physics = m2;
        chemistry = m3;
    }
    void print_marks(void)
    {
        cout << "your result is here: " << endl
             << "maths = " << maths << endl
             << "physics = " << physics << endl
             << "chemistry = " << chemistry << endl;
    }
};

class sports : virtual public student
{
protected:
    float score;

public:
    void set_score(int s)
    {
        score = s;
    }
    void print_score(void)
    {
        cout << "Your PT score is: " << score << endl;
    }
};

class result : public test, public sports
{
protected:
    float total;

public:
    void display(void)
    {
        total = maths + physics + chemistry + score;
        print_number();
        print_marks();
        print_score();
        cout << "Your total score is : " << total << endl;
    }
    void percentage()
    {
        float total_result;
        total_result = (maths + physics + chemistry + score) / 4;
        cout << "Your total percentage is: " << total_result << endl;
    }
};

int main()
{
    result hariom;
    hariom.set_number(10025);
    hariom.set_marks(89.45, 98.78, 100);
    hariom.set_score(90);
    hariom.display();
    hariom.percentage();
    return 0;
}