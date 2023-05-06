void main(List<String> args) {
  int radius = 10;
  double pi = 3.14;
  num area = pi * radius * radius;
  print("Area = $area");

  var num1 = int.parse("12");
  var num2 = num.parse("15.87");
  var ans = num1 + num2;
  print("Sum = $ans");

  BigInt value1 = BigInt.parse("886879887778766565");
  BigInt value2 = BigInt.parse("913456352536268282");
  BigInt product = value1 * value2;

  print("Product = $product");
}
