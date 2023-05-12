void main(List<String> args) {
  int a = 450;
  int b = 500;

  // convert int into string
  String a1 = a.toString();
  String b1 = b.toString();

  print("Concatenation = ${a1 + b1}");

  // convert string into int
  int a2 = int.parse(a1);
  int b2 = int.parse(b1);

  print("Sum = ${a2 + b2}");
}
