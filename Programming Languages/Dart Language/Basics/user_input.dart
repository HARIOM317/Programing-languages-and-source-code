import 'dart:ffi';
import 'dart:io';

void main(List<String> args) {
  stdout.write('Enter first number : ');
  int? a = int.parse(stdin.readLineSync()!);
  stdout.write('Enter second number : ');
  int? b = int.parse(stdin.readLineSync()!);
  int sum = a + b;
  stdout.write("Sum = $sum");
}
