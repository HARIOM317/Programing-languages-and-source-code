import 'dart:io';

void main(List<String> args) {
  print("Enter a number");
  int? num = int.parse(stdin.readLineSync()!);

  print("\nTable of $num is: \n");
  for (int i = 1; i <= 10; i++) {
    print("${num} * ${i} = ${num * i}");
  }
}
