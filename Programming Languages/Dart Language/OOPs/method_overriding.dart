class Human {
  void run() {
    print("Human is Running...");
  }
}

class Man extends Human {
  // method overriding
  void run() {
    print("Boy is Running...");
  }
}

void main(List<String> args) {
  Man m = new Man();
  m.run();
}
