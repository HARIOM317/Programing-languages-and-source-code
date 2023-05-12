class Student {
  static var branch;
  var name;
  var rollNo;

  // static method can access only static members
  static showBranch() {
    print("Student Branch is : $branch");
  }

  showDetails() {
    print("Name = $name");
    print("Roll Number = $rollNo");
    print("Branch = $branch");
  }
}

void main(List<String> args) {
  Student.branch = "CSE";
  Student.showBranch();

  Student std = Student();
  std.name = "Hariom";
  std.rollNo = 0537;

  std.showDetails();
}
