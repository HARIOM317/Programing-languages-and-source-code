/*
  Dart also provides the facility to specify a nameless function or function without a name. This type of function is known as an anonymous function, lambda, or closure. An anonymous function behaves the same as a regular function, but it does not have a name with it. It can have zero or any number of arguments with an optional type annotation.
 */

// lambda function
int add(int a, int b) => a + b;

void main(List<String> args) {
  print("Sum = ${add(10, 50)}");

  var list = ['C', 'C++', 'Java', 'Python', 'Dart', 'Javascript'];

  print("Dart Anonymous Function");
  // Anonymous Function
  list.forEach((item) {
    print("${list.indexOf(item)}: ${item}");
  });
}
