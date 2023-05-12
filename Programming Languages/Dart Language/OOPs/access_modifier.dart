class A {
  var first; // public variable
  var _second; // private variable (private means it is accessible in the library it is in and not accessible to other libraries.)

  void show() {
    print("First : $first");
    print("Second : $_second");
  }
}

class B extends A {
  void printFirst() {
    print(first);
  }

  void printSecond() {
    print(_second);
  }
}

void main(List<String> args) {
  B b = new B();
  b.first = "First String";
  b._second = "Second String";

  b.show();
  b.printFirst();
  b.printSecond();
}
