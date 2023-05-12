class Base {
  Base() {
    print("This is a Base class constructor");
  }

  void display() {
    print("Display method of Base class!");
  }
}

class Child extends Base {
  Child() : super() // calling super class constructor
  {
    print("This is a Child class constructor");
  }

  void display() {
    super.display();
    print("Display method of Child class!");
  }
}

void main(List<String> args) {
  Child c1 = new Child();
  c1.display();
}
