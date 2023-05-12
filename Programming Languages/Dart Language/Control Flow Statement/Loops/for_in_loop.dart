void main(List<String> args) {
  var list = [10, 25, 30, 45, 50, 65, 70, 85, 90, 100];
  int sum = 0;

  for (var element in list) {
    sum += element;
  }

  print("Sum = $sum");
}
