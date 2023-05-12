abstract class Person {
  void display();
}

class Boy extends Person {
  void display() {
    print("I am Boy!");
  }
}

class Girl extends Person {
  void display() {
    print("I am Girl!");
  }
}

void main(List<String> args) {
  Boy b = new Boy();
  b.display();

  Girl g = new Girl();
  g.display();
}
