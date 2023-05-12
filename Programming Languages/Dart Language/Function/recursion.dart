import 'dart:io';

int factorial(int n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1); // recursion
  }
}

void main(List<String> args) {
  print("Enter a Number");
  int? n = int.parse(stdin.readLineSync()!);
  print("Factorial of $n = ${factorial(n)}");
}
