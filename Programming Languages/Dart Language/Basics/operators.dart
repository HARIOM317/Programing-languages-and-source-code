void main(){
  int a = 2;
  int b = 3;

  //  Arithmetic operators (+, -, -expr, *, /, ~/, %)
  print("\nArithmetic Operator");
  var sum = a+b;
  print("Sum =  $sum");
  var diff = a-b;
  print("Difference =  $diff");
  var mul = a*b;
  print("Product =  $mul");
  var div = a/b;
  print("Division =  $div");
  var rem = a%b;
  print("Remainder = $rem");
  var quot = a~/b;
  print("Quotient = $quot");

  // Relational Operator (>, <, <=, >=, ==, !=)
  print("\nRelational Operator");
  print(a>b);
  print(a<b);
  print(a==b);
  print(a!=b);
  print(a>=b);

  // Test Operator (is, is!)
  print("\nTest Operator");
  String name = "Hariom";
  print(name is String);
  print(a is !int);

  // Bitwise Operator (&, |, ^, ~, <<, >>)
  print("\nBitwise Operator");
  print(a&b);
  print(a|b);
  print(a^b);
  print(~a);
  print(a<<b);
  print(a>>b);

  // Assignment Operator (=, ??=)
  print("\nAssignment Operator");
  var d;
  d??= a-b;
  print(d);
  d??=a+b;
  print(d);

  // Logical Operator (&&, ||, !)
  print("\nLogical Operator");
  print(a>10 && b <10);
  print(!(a>10));
  print(a>10 || b<10);

  // Conditional Operator (? :)
  print("\nConditional Operator");
  var c = (a<10) ? "Statement is correct" : "Statement is wrong";
  print(c);
}