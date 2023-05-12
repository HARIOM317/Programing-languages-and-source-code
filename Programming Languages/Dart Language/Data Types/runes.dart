/*
  As we discussed earlier, Dart String is a sequence of characters, letters, numbers, and unique characters. It is the sequence of UTF - 16 Unicode characters where Dart Runes are the sequence UTF - 32 Unicode code points. It is a UTF-32 string which is used to print the special symbol. For example - The theta (Θ) symbol is signified by using the corresponding Unicode equivalent \u0398; here '\u' refers to Unicode, and the numbers are in the hexadecimal. Sometimes the hex digits are the more than 4 digits then it should be placed in curly brackets ({}).
 */

void main(List<String> args) {
  var heart = "\u2665";
  var theta = "\u0398";
  var emogi1 = "\u{1f600}";
  var emogi2 = "\u{1f601}";
  var emogi3 = "\u{1f602}";
  var emogi4 = "\u{1f603}";
  var emogi5 = "\u{1f604}";

  print(heart);
  print(theta);
  print(emogi1);
  print(emogi2);
  print(emogi3);
  print(emogi4);
  print(emogi5);

  // Methods

  String str = "Hariom";

  // 1. codeUnitAt()
  print(str.codeUnitAt(0));

  // 2. codeUnits
  print(str.codeUnits);
}
