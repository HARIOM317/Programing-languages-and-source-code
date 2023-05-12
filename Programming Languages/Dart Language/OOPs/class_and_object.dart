class Employee {
  var name;
  var id;
  var age;
  var salary;
  var domain;
  var experiencePOfYear;

  showInfo() {
    print("Employee name is : ${name}");
    print("Employee id is : ${id}");
    print("Employee age is : ${age}");
    print("Employee salary is : ${salary}");
    print("Employee domain is : ${domain}");
    print("Employee experiencePOfYear is : ${experiencePOfYear}");
  }
}

void main(List<String> args) {
  var emp = new Employee();
  emp.name = "Hariom";
  emp.id = 201022;
  emp.age = 22;
  emp.salary = 25000000;
  emp.domain = "AI/ML";
  emp.experiencePOfYear = 2;

  emp.showInfo();
}
