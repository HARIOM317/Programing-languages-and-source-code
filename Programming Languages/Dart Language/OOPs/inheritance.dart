class Person {
  var name;
  var age;
  var gender;

  void showData() {
    print("Name : $name");
    print("Age : $age");
    print("Gender : $gender");
  }
}

class Alok extends Person {
  var nationality;
  Alok(var nationality) {
    this.nationality = nationality;
    print("\nNationality : $nationality");
  }
}

class Pooja extends Person {
  var qualification;
  Pooja(var qualification) {
    this.qualification = qualification;
    print("\nQualification : $qualification");
  }
}

void main(List<String> args) {
  Alok alok = new Alok("Canadian");
  alok.name = "ALOK";
  alok.age = 20;
  alok.gender = "MALE";
  alok.showData();

  Pooja pooja = new Pooja("MBA");
  pooja.name = "POOJA";
  pooja.age = 19;
  pooja.gender = "FEMALE";
  pooja.showData();
}
