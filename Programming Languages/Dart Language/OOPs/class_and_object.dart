void main(List<String> args) {
  Employee emp1 = new Employee();
  emp1.setName("Hariom");
  String name = emp1.getName();
  print("Employee = $name");
}

class Employee {
  String name = "";
  Employee() {
    print("Default constructor called!");
  }
  void setName(String name) {
    this.name = name;
  }

  String getName() {
    return this.name;
  }
}
