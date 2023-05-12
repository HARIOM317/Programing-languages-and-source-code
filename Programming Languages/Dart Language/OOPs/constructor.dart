/*
  Types of Constructors in dart:
  There are three types of constructors in Dart as given below.

  1. Default Constructor or no-arg Constructor
  2. Parameter Constructor
  3. Named Constructor
*/

class Student {
  // default constructor
  Student() {
    print("\n<<< Default Constructor of class Student! >>>\n");
  }

  // named constructor with name info - The named constructors are used to declare the multiple constructors in single class.
  Student.info(String name, String department, int year) {
    print("<<< Named Constructor >>>");
    print("Name : $name");
    print("Department : $department");
    print("Year : $year");
  }
}

void main(List<String> args) {
  Student();
  Student.info("Hariom", "CSE", 2);
}
