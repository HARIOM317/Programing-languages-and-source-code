import 'dart:io';

bool isPrime(int n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

void main(List<String> args) {
  print("Enter a number");
  int? n = int.parse(stdin.readLineSync()!);

  if (isPrime(n)) {
    print("Prime Number");
  } else {
    print("Non Prime Number");
  }
}
