void main(List<String> args) {
  // single quoted string
  String str = 'This is single quoted string\n';
  print(str);

  // double quoted string
  String name = "He Guys!";
  var profession = "$name, This is an example of double quoted string";
  print(profession);

  // multi line string
  String msg = """\nHello Everyone!
  This is an example of...
  Multiline String in DART""";
  print(msg);

  // row string
  var rawStr = r'This is a raw String';
  print("\n$rawStr");
}
