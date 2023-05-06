#include <iostream>

using namespace std;

class Student
{
private:
    int id;

protected:
    float marks;

public:
    string name;

    void setId(int id)
    {
        this->id = id;
    }

    int getId()
    {
        return this->id;
    }

    void showData()
    {
        cout << "\nStudent name : " << this->name << endl;
        cout << "Student id : " << this->id << endl;
        cout << "Student marks : " << this->marks << endl;
    }
};

class Result : public Student
{
public:
    Result(float marks)
    {
        this->marks = marks;
    }
};

int main()
{
    Result s1(93.78);
    s1.name = "Hariom Singh Rajput";
    s1.setId(1005);

    s1.showData();

    return 0;
}