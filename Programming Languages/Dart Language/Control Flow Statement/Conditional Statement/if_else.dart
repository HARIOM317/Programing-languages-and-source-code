import 'dart:ffi';
import 'dart:io';

void main(List<String> args) {
  print("\nEnter marks of math : ");
  int? math = int.parse(stdin.readLineSync()!);
  print("Enter marks of science : ");
  int? science = int.parse(stdin.readLineSync()!);
  print("Enter marks of computer : ");
  int? computer = int.parse(stdin.readLineSync()!);

  var result = (math + science + computer) / 3;
  print("\nResult = ${result}");

  // conditional statement
  if (result < 33) {
    print("Fail");
  } else if (result >= 33 && result < 45) {
    print("Grade D");
  } else if (result >= 45 && result < 60) {
    print("Grade C");
  } else if (result >= 60 && result < 75) {
    print("Grade B");
  } else if (result >= 75 && result < 85) {
    print("Grade A");
  } else if (result >= 85 && result < 100) {
    print("Grade A+");
  } else {
    print("Excellent!");
  }
}
