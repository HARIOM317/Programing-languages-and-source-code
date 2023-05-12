import 'dart:io';

void main(List<String> args) {
  print("Enter your favorite color");
  String? color = stdin.readLineSync();

  switch (color) {
    case "red":
      print("Your Favorite Color is Red");
      break;
    case "blue":
      print("Your Favorite Color is Blue");
      break;
    case "white":
      print("Your Favorite Color is White");
      break;
    case "black":
      print("Your Favorite Color is Black");
      break;
    case "orange":
      print("Your Favorite Color is Orange");
      break;
    default:
      print("You Like $color Color");
      break;
  }
}
