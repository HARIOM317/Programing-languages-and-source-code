class Employee {
  void profession() {
    print("I am working as an Engineer");
  }

  void salary(int salary) {
    print("My salary is : $salary");
  }
}

// Defining interface by implanting another class
class Engineer implements Employee {
  void profession() {
    print("Profession : Engineering");
  }

  void salary(int salary) {
    print("Salary : $salary");
  }
}

void main(List<String> args) {
  Engineer eng = new Engineer();
  eng.profession();
  eng.salary(8000000);

  Employee emp = new Engineer();
  emp.profession();
  emp.salary(100000000);
}
